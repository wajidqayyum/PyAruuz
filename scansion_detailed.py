from scansion import Scansion
from meters import Meters
import math
import re

class ScansionDetailed(Scansion):
    def code_to_num(self, code_str, target_ref=""):
        res = ""
        for idx, c in enumerate(code_str):
            if c == '=':
                res += "2"
            elif c == '-':
                res += "1"
            elif c == 'x':
                if idx < len(target_ref):
                    res += "1" if target_ref[idx] == '-' else "2"
                else:
                    res += "2"
            elif c == '~':
                res += "21"
        return res

    def get_word_syllables(self, word, code_len):
        if code_len == 0:
            return []
        clean_w = re.sub(r'[،۔؟!؛()\'"\-]', '', word)
        if code_len == 1 or len(clean_w) <= 1:
            return [clean_w]
            
        cur = self.db.cursor()
        cur.execute("SELECT Taqti FROM mastertable WHERE Word = ? LIMIT 1", (clean_w,))
        row = cur.fetchone()
        if row and row[0]:
            raw_taqti = row[0]
            clean_taqti = re.sub(r'[\u064B-\u0652\u0670]', '', raw_taqti)
            parts = [p.strip() for p in clean_taqti.split('+') if p.strip()]
            if len(parts) == code_len:
                return parts

        if code_len == 2:
            if len(clean_w) == 2:
                return [clean_w[0], clean_w[1]]
            elif len(clean_w) == 3:
                if clean_w[1] in ['ا', 'و', 'ی', 'ے']:
                    return [clean_w[:2], clean_w[2:]]
                elif clean_w[0] not in ['ا', 'و', 'ی', 'ے'] and clean_w[1] in ['ی'] and clean_w[2] == 'ا': # e.g. گیا
                    return [clean_w[:1], clean_w[1:]]
                else:
                    return [clean_w[:1], clean_w[1:]]
            elif len(clean_w) == 4:
                return [clean_w[:2], clean_w[2:]]
            else:
                mid = len(clean_w) // 2
                return [clean_w[:mid], clean_w[mid:]]
                
        if code_len == 3:
            if len(clean_w) == 3:
                return [clean_w[0], clean_w[1], clean_w[2]]
            elif len(clean_w) == 4:
                if clean_w[1] in ['ا', 'و', 'ی', 'ے']:
                    return [clean_w[:2], clean_w[2:3], clean_w[3:]]
                else:
                    return [clean_w[:1], clean_w[1:3], clean_w[3:]]
            elif len(clean_w) == 5:
                return [clean_w[:2], clean_w[2:4], clean_w[4:]]
            else:
                p1 = len(clean_w) // 3
                p2 = 2 * p1
                return [clean_w[:p1], clean_w[p1:p2], clean_w[p2:]]

        res = []
        chunk_size = max(1, len(clean_w) // code_len)
        start = 0
        for i in range(code_len):
            if i == code_len - 1:
                res.append(clean_w[start:])
            else:
                end = start + chunk_size
                res.append(clean_w[start:end])
                start = end
        return res

    def get_diagnostic_suggestions(self, line, words, dominant_meter, target_variant):
        suggestions = []
        # 1. Check Izafat (Zer)
        for i, w in enumerate(words):
            if len(w) > 1 and not w.endswith('ِ') and not w.endswith('ۂ'):
                izafat_mark = 'ۂ' if w.endswith('ہ') or w.endswith('ی') else 'ِ'
                mod_words = list(words)
                mod_words[i] = w + izafat_mark
                mod_line = " ".join(mod_words)
                mod_codes = self.get_line_word_codes(mod_line)
                _, test_dist, _ = self._fuzzy_dp_match(mod_codes, target_variant)
                if test_dist == 0:
                    suggestions.append({
                        "type": "izafat",
                        "title": "اعراب (اضافت)",
                        "desc": f"اگر «{w}» پر اضافت ہے ({w + izafat_mark}) تو مصرعہ وزن میں ہے",
                        "fixed_line": mod_line
                    })
                    break

        # 2. Syllable count diagnostic
        target_len = len(target_variant)
        line_codes = self.get_line_word_codes(line)
        _, _, chosen_list = self._fuzzy_dp_match(line_codes, target_variant)
        actual_len = sum(len(c) for c in chosen_list)
        if actual_len < target_len:
            diff = target_len - actual_len
            suggestions.append({
                "type": "count",
                "title": "ہجوں کی کمی",
                "desc": f"مصرعے میں {actual_len} ہجے ہیں، اس بحر کو {target_len} چاہئیں — {diff} ہجا کم ہے۔"
            })
        elif actual_len > target_len:
            diff = actual_len - target_len
            suggestions.append({
                "type": "count",
                "title": "ہجوں کی زیادتی",
                "desc": f"مصرعے میں {actual_len} ہجے ہیں، اس بحر کو {target_len} چاہئیں — {diff} ہجا زیادہ ہے۔"
            })
        else:
            suggestions.append({
                "type": "order",
                "title": "ہجوں کی ترتیب",
                "desc": f"ہجوں کی تعداد ({target_len}) ٹھیک ہے مگر ترتیب بحر سے نہیں ملتی (کہیں طویل کی جگہ خفیف یا خفیف کی جگہ طویل ہجا ہے)۔"
            })

        return suggestions

    def get_other_meters(self, line_word_codes, exclude_meter):
        other = []
        seen = set([exclude_meter])
        for idx, m_name in enumerate(Meters.meter_names):
            if m_name in seen: continue
            m_raw = Meters.meters[idx].replace("/", "").replace("+", "")
            _, dist, _ = self._fuzzy_dp_match(line_word_codes, m_raw)
            if dist <= 3:
                seen.add(m_name)
                # feet
                feet = []
                for chunk in Meters.meters[idx].split('/'):
                    c_clean = chunk.replace("+", "")
                    if c_clean in Meters.feet:
                        feet.append(Meters.feet_names[Meters.feet.index(c_clean)])
                other.append({
                    "meter_name": m_name,
                    "feet_names": feet,
                    "distance": dist
                })
                if len(other) >= 6:
                    break
        return other

    def scan_poem_detailed(self, text, selected_meter=None, mode="ghazal"):
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        if not lines:
            return {"dominant_meter": "", "lines": [], "stats": {}}
            
        # Determine meter variants
        meter_variants = {}
        for idx, m_name in enumerate(Meters.meter_names):
            if m_name not in meter_variants:
                meter_variants[m_name] = []
            meter_variants[m_name].append(Meters.meters[idx].replace("/", "").replace("+", ""))

        best_overall_meter = None
        if selected_meter and selected_meter != "خودکار":
            best_overall_meter = selected_meter
        elif mode == "ghazal":
            first_line_word_codes = self.get_line_word_codes(lines[0])
            candidate_names = set()
            for idx, meter in enumerate(Meters.meters):
                m_raw = meter.replace("/", "").replace("+", "")
                _, dist, _ = self._fuzzy_dp_match(first_line_word_codes, m_raw)
                if dist <= 5:
                    candidate_names.add(Meters.meter_names[idx])
            
            meter_line_scores = {m: [] for m in candidate_names}
            for line in lines:
                line_word_codes = self.get_line_word_codes(line)
                for m_name in candidate_names:
                    best_dist_for_name = 100
                    for m_raw in meter_variants[m_name]:
                        _, dist, _ = self._fuzzy_dp_match(line_word_codes, m_raw)
                        if dist < best_dist_for_name:
                            best_dist_for_name = dist
                    meter_line_scores[m_name].append(best_dist_for_name if best_dist_for_name != 100 else 99)
            
            min_final_score = float('inf')
            for m_name, dists in meter_line_scores.items():
                score, count, subtract = 0.0, 0.0, 0.0
                for d in dists:
                    if d == 0:
                        score += math.log(d + 1)
                        count += 1.0
                        subtract += 1.0
                    else:
                        score += math.log(d)
                        count += 1.0
                if count == 0: continue
                final_score = math.exp(score / count) - subtract
                if final_score < min_final_score:
                    min_final_score = final_score
                    best_overall_meter = m_name

        if not best_overall_meter and mode == "ghazal":
            best_overall_meter = Meters.meter_names[0]

        poem_results = []
        in_meter_count = 0
        out_meter_count = 0

        for line in lines:
            line_words = line.split()
            line_word_codes = self.get_line_word_codes(line)
            
            line_meter = best_overall_meter
            if mode == "nazm":
                # find best meter for this line independently
                b_dist = 100
                for idx, m_name in enumerate(Meters.meter_names):
                    m_raw = Meters.meters[idx].replace("/", "").replace("+", "")
                    _, dist, _ = self._fuzzy_dp_match(line_word_codes, m_raw)
                    if dist < b_dist:
                        b_dist = dist
                        line_meter = m_name
                        if dist == 0: break

            # Find best variant under line_meter
            best_dist = 100
            best_variant_raw = ""
            best_variant_code = ""
            best_variant_list = []
            for m_raw in meter_variants.get(line_meter, [Meters.meters[0].replace("/", "")]):
                matched_code, dist, code_list = self._fuzzy_dp_match(line_word_codes, m_raw)
                if dist < best_dist:
                    best_dist = dist
                    best_variant_raw = m_raw
                    best_variant_code = matched_code
                    best_variant_list = code_list

            original_variant = ""
            for idx, m_name in enumerate(Meters.meter_names):
                if m_name == line_meter and Meters.meters[idx].replace("/", "").replace("+", "") == best_variant_raw:
                    original_variant = Meters.meters[idx]
                    break
            if not original_variant:
                original_variant = Meters.meters[0]

            feet_names_arr = []
            for chunk in original_variant.split('/'):
                chunk_clean = chunk.replace("+", "")
                if chunk_clean in Meters.feet:
                    feet_names_arr.append(Meters.feet_names[Meters.feet.index(chunk_clean)])
                else:
                    feet_names_arr.append("؟")

            # Construct word codes
            word_codes_mapped = []
            list_idx = 0
            for idx, w in enumerate(line_words):
                if list_idx < len(best_variant_list):
                    mapped_c = best_variant_list[list_idx]
                    word_codes_mapped.append(mapped_c if mapped_c else " ")
                    list_idx += 1
                else:
                    word_codes_mapped.append(" ")

            # Words Breakdown & Syllable Array
            all_syllables = []
            words_breakdown = []
            curr_pos = 0

            for w, c in zip(line_words, word_codes_mapped):
                c_clean = c.strip()
                k = len(c_clean)
                target_slice = best_variant_raw[curr_pos:curr_pos+k]
                w_num = self.code_to_num(c_clean, target_slice)
                words_breakdown.append({
                    "word": w,
                    "weight_num": w_num if w_num else "-",
                    "code": c_clean
                })
                syls = self.get_word_syllables(w, k)
                for s_idx, s in enumerate(syls):
                    s_weight = "2"
                    if s_idx < len(c_clean):
                        char = c_clean[s_idx]
                        if char == '=': s_weight = "2"
                        elif char == '-': s_weight = "1"
                        elif char == 'x':
                            s_pos = curr_pos + s_idx
                            if s_pos < len(best_variant_raw) and best_variant_raw[s_pos] == '-':
                                s_weight = "1"
                            else:
                                s_weight = "2"
                    all_syllables.append({"text": s, "weight": s_weight})
                curr_pos += k

            # Partition into Arkan
            syl_idx = 0
            arkan = []
            chunks = original_variant.split('/')
            for ch, fn in zip(chunks, feet_names_arr):
                ch_clean = ch.replace('+', '')
                l = len(ch_clean)
                r_syls = all_syllables[syl_idx:syl_idx+l]
                syl_idx += l
                arkan.append({
                    "name": fn,
                    "weight_num": self.code_to_num(ch_clean),
                    "code": ch_clean,
                    "syllables": r_syls
                })

            # Check if any remaining syllables
            if syl_idx < len(all_syllables) and arkan:
                arkan[-1]["syllables"].extend(all_syllables[syl_idx:])

            is_in_meter = (best_dist == 0)
            if is_in_meter:
                in_meter_count += 1
            else:
                out_meter_count += 1

            # Suggestions if out of meter
            suggestions = []
            if not is_in_meter:
                suggestions = self.get_diagnostic_suggestions(line, line_words, line_meter, best_variant_raw)

            # Other meters
            other_meters = self.get_other_meters(line_word_codes, line_meter)

            poem_results.append({
                "line": line,
                "words": line_words,
                "codes": word_codes_mapped,
                "words_breakdown": words_breakdown,
                "arkan": arkan,
                "meter_name": line_meter,
                "feet_names": feet_names_arr,
                "distance": best_dist,
                "is_in_meter": is_in_meter,
                "matched_code": best_variant_code,
                "suggestions": suggestions,
                "other_meters": other_meters
            })

        # Overall feet names for dominant meter
        dominant_feet_names = []
        if poem_results:
            dominant_feet_names = poem_results[0]["feet_names"]

        return {
            "dominant_meter": best_overall_meter,
            "dominant_feet_names": dominant_feet_names,
            "lines": poem_results,
            "stats": {
                "total": len(lines),
                "in_meter": in_meter_count,
                "out_meter": out_meter_count
            }
        }
