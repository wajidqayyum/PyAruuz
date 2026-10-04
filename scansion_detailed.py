from scansion import Scansion
from meters import Meters
import math

class ScansionDetailed(Scansion):
    def scan_poem_detailed(self, text):
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        if not lines: return {"dominant_meter": "", "lines": []}
        meter_line_scores = {}
        
        first_line_word_codes = self.get_line_word_codes(lines[0])
        candidate_names = set()
        for idx, meter in enumerate(Meters.meters):
            m_raw = meter.replace("/", "").replace("+", "")
            _, dist, _ = self._fuzzy_dp_match(first_line_word_codes, m_raw)
            if dist <= 5: candidate_names.add(Meters.meter_names[idx])
        
        for m_name in candidate_names: meter_line_scores[m_name] = []
        meter_variants = {}
        for idx, m_name in enumerate(Meters.meter_names):
            if m_name in candidate_names:
                if m_name not in meter_variants: meter_variants[m_name] = []
                meter_variants[m_name].append(Meters.meters[idx].replace("/", "").replace("+", ""))
                
        for line in lines:
            line_word_codes = self.get_line_word_codes(line)
            for m_name in candidate_names:
                best_dist_for_name = 100
                for m_raw in meter_variants[m_name]:
                    _, dist, _ = self._fuzzy_dp_match(line_word_codes, m_raw)
                    if dist < best_dist_for_name: best_dist_for_name = dist
                if best_dist_for_name == 100: best_dist_for_name = 99
                meter_line_scores[m_name].append(best_dist_for_name)
        
        best_overall_meter = None
        min_final_score = float('inf')
        for m_name, dists in meter_line_scores.items():
            score = 0.0
            count = 0.0
            subtract = 0.0
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
        
        if not best_overall_meter: return {"dominant_meter": "", "lines": []}
        
        poem_results = []
        for line in lines:
            line_words = line.split()
            line_word_codes = self.get_line_word_codes(line)
            
            best_dist = 100
            best_variant_raw = ""
            best_variant_code = ""
            best_variant_list = []
            for m_raw in meter_variants[best_overall_meter]:
                matched_code, dist, code_list = self._fuzzy_dp_match(line_word_codes, m_raw)
                if dist < best_dist:
                    best_dist = dist
                    best_variant_raw = m_raw
                    best_variant_code = matched_code
                    best_variant_list = code_list
            
            original_variant = ""
            for idx, m_name in enumerate(Meters.meter_names):
                if m_name == best_overall_meter and Meters.meters[idx].replace("/", "").replace("+", "") == best_variant_raw:
                    original_variant = Meters.meters[idx]
                    break
            
            feet_names_arr = []
            for chunk in original_variant.split('/'):
                chunk_clean = chunk.replace("+", "")
                if chunk_clean in Meters.feet:
                    feet_names_arr.append(Meters.feet_names[Meters.feet.index(chunk_clean)])
                else:
                    feet_names_arr.append("؟")
                    
            word_codes_mapped = []
            # We now have exactly the codes picked by the DP in `best_variant_list`.
            # We just need to map them to the original words.
            list_idx = 0
            for idx, w in enumerate(line_words):
                # The w_codes represents the set of possible codes for this word.
                # If the word's code was completely wiped (e.g., Waw), its code set contains `""`.
                # Did the DP pick `""`? If so, `best_variant_list` will have `""`.
                w_codes = line_word_codes[idx]
                if list_idx < len(best_variant_list):
                    mapped_c = best_variant_list[list_idx]
                    word_codes_mapped.append(mapped_c if mapped_c else " ")
                    list_idx += 1
                else:
                    word_codes_mapped.append(" ")
                    
            poem_results.append({
                "line": line,
                "words": line_words,
                "codes": word_codes_mapped,
                "meter_name": best_overall_meter,
                "feet_names": feet_names_arr,
                "distance": best_dist,
                "matched_code": best_variant_code
            })
            
        return {"dominant_meter": best_overall_meter, "lines": poem_results}
