import re
import itertools
from araab import Araab
from meters import Meters
import heuristics

class Scansion:
    def __init__(self, db_connection):
        self.db = db_connection

    def _query_db(self, word):
        cursor = self.db.cursor()
        
        cursor.execute("SELECT Code, Taqti2, Taqti3 FROM exceptions WHERE Word = ?", (word,))
        row = cursor.fetchone()
        if row:
            codes = []
            if row[0]: codes.append(row[0].replace('0', '-').replace('1', '=').replace(' ', '').lower())
            if row[1]: codes.append(row[1].replace('0', '-').replace('1', '=').replace(' ', '').lower())
            if row[2]: codes.append(row[2].replace('0', '-').replace('1', '=').replace(' ', '').lower())
            return codes, ""
            
        cursor.execute("SELECT Taqti, Language FROM mastertable WHERE Word = ?", (word,))
        row = cursor.fetchone()
        if row: return [self._get_root_code(row[0] or '')], row[1]
        
        return [], ""

    def _get_root_code(self, muarrab):
        muarrab = muarrab.strip()
        # Apply Tashdid rewriting before scanning
        muarrab = Araab.remove_tashdid(muarrab)
        chunks = [x.strip() for x in muarrab.split('+')]
        code = ''
        for chunk in chunks:
            stripped = Araab.remove_araab(chunk.replace("\u06BE", "").replace("\u06BA", ""))
            n = len(stripped)
            chunk_code = ""
            if n == 1: chunk_code = heuristics.length_one_scan(chunk)
            elif n == 2: chunk_code = heuristics.length_two_scan(chunk)
            elif n == 3: chunk_code = heuristics.length_three_scan(chunk)
            elif n == 4: chunk_code = heuristics.length_four_scan(chunk)
            elif n == 5: chunk_code = heuristics.length_five_scan(chunk)
            else: chunk_code = "=" * (n // 2) + ("-" if n % 2 else "")
            
            if heuristics.contains_noon(chunk):
                chunk_code = heuristics.noon_ghunna(chunk, chunk_code)
                
            code += chunk_code
        return code

    def _apply_terminal_vowel_rule(self, word, code, language, is_modified):
        if not code: return code
        if not heuristics.is_vowel_plus_h(word[-1]): return code
        
        if code[-1] in ['=', 'x']:
            if word[-1] in ['ا', 'ی']:
                if language == "عربی" and not is_modified: return code[:-1] + '='
                if language == "فارسی" and word[-1] == 'ا' and not is_modified: return code[:-1] + '='
                return code[:-1] + 'x'
            elif word[-1] in ['ے', 'و', 'ہ', 'ؤ']:
                return code[:-1] + 'x'
        return code

    def _resolve_by_suffix(self, s):
        # Implementation of Unknown Word Guesswork
        codes = []
        n = len(s)
        
        def mutate_code(base_code, suffix_type):
            if not base_code: return ""
            res = ""
            if suffix_type == 'ں': res = base_code[:-1] if base_code[-1] == '-' else base_code
            if suffix_type == 'ئے':
                return base_code[:-1] + '=x' if base_code[-1] == 'x' else base_code + 'x'
            if suffix_type == 'تا':
                return base_code[:-1] + '=x' if base_code[-1] == 'x' else base_code + 'x'
            if suffix_type == 'تیں':
                return base_code[:-1] + '=x' if base_code[-1] == 'x' else base_code + 'x'
            if suffix_type == 'نا':
                return base_code[:-1] + '=x' if base_code[-1] == 'x' else base_code + 'x'
            if suffix_type == 'ئیں':
                return base_code[:-1] + '=x' if base_code[-1] == 'x' else base_code + 'x'
            if suffix_type == 'vowel':
                if base_code[-1] == '-': return base_code[:-1] + 'x'
                if base_code.endswith('=-'): return base_code[:-2] + '=x'
                if base_code.endswith('=='): return base_code[:-2] + '-x'
                return base_code
            if suffix_type == 'ات':
                if base_code[-1] in ['=', 'x']: return base_code[:-1] + '-=-'
                if base_code[-1] == '-': return base_code[:-1] + '=-'
                return base_code
            if suffix_type == 'وں':
                if base_code[-1] in ['=', 'x']: return [base_code[:-1] + '-x', base_code[:-1] + '=x']
                if base_code[-1] == '-': return [base_code[:-1] + 'x']
                return [base_code]
            if suffix_type == 'ان':
                if base_code[-1] == '-': return base_code[:-1] + '=-'
                return base_code + '-=-'
            if suffix_type == 'ال':
                return '=' + base_code
            if not res: res = base_code
            return res

        # Attempt different suffix strips
        if n > 3 and s.endswith('ں'):
            bcs, lang = self._query_db(s[:-1] + 'ن')
            if not bcs: bcs, lang = self._query_db(s[:-1])
            for bc in bcs: codes.append(mutate_code(bc, 'ں'))
        
        if n > 4 and s.endswith('ئے'):
            bcs, lang = self._query_db(s[:-2])
            if not bcs: bcs, lang = self._query_db(s[:-2] + 'نا')
            for bc in bcs: codes.append(mutate_code(bc, 'ئے'))
            
        if n > 3 and s.endswith(('تا', 'تے', 'تی')):
            bcs, lang = self._query_db(s[:-2])
            if not bcs: bcs, lang = self._query_db(s[:-2] + 'نا')
            for bc in bcs: codes.append(mutate_code(bc, 'تا'))
            
        if n > 3 and s.endswith('تیں'):
            bcs, lang = self._query_db(s[:-3])
            if not bcs: bcs, lang = self._query_db(s[:-3] + 'نا')
            for bc in bcs: codes.append(mutate_code(bc, 'تیں'))
            
        if n > 4 and s.endswith(('نا', 'نے', 'نی')):
            bcs, lang = self._query_db(s[:-2])
            if not bcs: bcs, lang = self._query_db(s[:-2] + 'نا')
            for bc in bcs: codes.append(mutate_code(bc, 'نا'))
            
        if n > 4 and s.endswith('ئیں'):
            # Specific check for nouns like بلائیں (root بلا)
            bcs, lang = self._query_db(s[:-3])
            if not bcs: 
                bcs, lang = self._query_db(s[:-3] + 'نا')
            for bc in bcs: 
                codes.append(mutate_code(bc, 'ئیں'))
            
        if n > 4 and s.endswith(('ا', 'ے', 'ی', 'و', 'ہ', 'ؤ')):
            bcs, lang = self._query_db(s[:-1])
            if not bcs: bcs, lang = self._query_db(s[:-1] + 'نا')
            for bc in bcs: codes.append(mutate_code(bc, 'vowel'))
            
        if n > 4 and s.endswith(('ات', 'یات', 'ئیات')):
            bcs, lang = self._query_db(s[:-2])
            for bc in bcs: codes.append(mutate_code(bc, 'ات'))
            
        if n > 4 and s.endswith(('وں', 'اں', 'یں', 'ؤں')):
            bcs, lang = self._query_db(s[:-2])
            for bc in bcs:
                res = mutate_code(bc, 'وں')
                if isinstance(res, list): codes.extend(res)
                else: codes.append(res)
                
        if n > 2 and s.endswith('ان'):
            bcs, lang = self._query_db(s[:-2])
            for bc in bcs: codes.append(mutate_code(bc, 'ان'))
            
        if n > 1 and s.startswith('ال'):
            bcs, lang = self._query_db(s[2:])
            for bc in bcs: codes.append(mutate_code(bc, 'ال'))
            
        return codes

    def get_word_codes(self, word):
        clean_word = re.sub(r'[،۔؟!؛()\'"\-]', '', word)
        db_search_word = Araab.remove_araab(clean_word)
        if not db_search_word: return []
        
        codes = []
        is_modified = False
        
        # 1. DB Lookup
        bcs, lang = self._query_db(db_search_word)
        if bcs:
            for bc in bcs:
                codes.append(self._apply_terminal_vowel_rule(clean_word, bc, lang, False))
                
        # 2. Suffix Resolution (Try even if DB match found, as DB might be rigid)
        suffix_codes = self._resolve_by_suffix(clean_word)
        if suffix_codes:
            for sc in suffix_codes:
                codes.append(self._apply_terminal_vowel_rule(clean_word, sc, "", True))
                
        # 3. Root Heuristic Scan (Raw scan ignoring DB Araab)
        h_code = self._get_root_code(clean_word)
        if h_code:
            codes.append(self._apply_terminal_vowel_rule(clean_word, h_code, "", True))
                
        # 4. Global Rule: Noon Ghunna Internal weighting
        if heuristics.contains_noon(db_search_word):
            codes = [heuristics.noon_ghunna(clean_word, c) for c in codes]

        return list(set([c for c in codes if c and ' ' not in c]))

    def get_line_word_codes(self, line):
        words = line.split()
        line_word_codes = []
        for word in words:
            codes = self.get_word_codes(word)
            line_word_codes.append(codes if codes else [""])

        # 5. Line-Level Poetic Combinations
        for i in range(1, len(words)):
            w2 = words[i]
            w1 = words[i-1]
            w2_clean = Araab.remove_araab(w2.replace("\u06BE", "").replace("\u06BA", ""))
            w1_clean = Araab.remove_araab(w1.replace("\u06BE", "").replace("\u06BA", ""))
            
            # A. Alif-Lam (ال) Rule
            if w2_clean.startswith('ال'):
                # Check if w1 ends in Zabar or Pesh
                w1_loc = heuristics.locate_araab(w1)
                if len(w1_loc) > 0 and w1_loc[-1] in [Araab.characters[8], Araab.characters[9]]:
                    new_w1_codes = []
                    for c in line_word_codes[i-1]:
                        if not c: continue
                        if heuristics.is_vowel_plus_h(w1_clean[-1]):
                            if c[-1] in ['=', 'x', '-']: new_w1_codes.append(c[:-1] + '=')
                        else:
                            if len(w1_clean) == 2 and heuristics.is_consonant_plus_consonant(w1_clean):
                                new_w1_codes.append(c + '==') # Simplified
                            else:
                                if c[-1] in ['=', 'x']: new_w1_codes.append(c[:-1] + '-=')
                                elif c[-1] == '-': new_w1_codes.append(c[:-1] + '=')
                    line_word_codes[i-1] = list(set(line_word_codes[i-1] + new_w1_codes))
                    # Remove Alif from w2
                    new_w2_codes = []
                    for c in line_word_codes[i]:
                        if c: new_w2_codes.append(c[1:])
                    line_word_codes[i] = list(set(line_word_codes[i] + new_w2_codes))
                    
            # B. Izafat
            if heuristics.is_izafat(w1):
                new_w1_codes = []
                for c in line_word_codes[i-1]:
                    if not c: continue
                    if len(w1_clean) == 2 and not heuristics.is_vowel_plus_h(w1_clean[1]):
                        new_w1_codes.append(c[:-1] + 'xx')
                    elif c[-1] in ['=', 'x']:
                        if w1_clean[-1] in ['ا', 'و']: new_w1_codes.append(c[:-1] + '=x')
                        elif w1_clean[-1] == 'ی': 
                            new_w1_codes.append(c[:-1] + '-x')
                            new_w1_codes.append(c[:-1] + '=x')
                        else: new_w1_codes.append(c[:-1] + '-x')
                    elif c[-1] == '-':
                        new_w1_codes.append(c[:-1] + 'x')
                line_word_codes[i-1] = list(set(line_word_codes[i-1] + new_w1_codes))
                
            # C. Ataf (و)
            if w2_clean == 'و':
                new_w1_codes = []
                for c in line_word_codes[i-1]:
                    if not c: continue
                    if w1_clean[-1] in ['ا', 'ی']: new_w1_codes.append(c)
                    elif w1_clean[-1] in ['ے', 'و']:
                        if c[-1] in ['=', 'x']: new_w1_codes.append(c[:-1] + '-x')
                        elif c[-1] == '-': new_w1_codes.append(c[:-1] + 'x')
                    else:
                        if len(w1_clean) == 2 and heuristics.is_consonant_plus_consonant(w1_clean):
                            new_w1_codes.append(c[:-1] + 'xx')
                        elif c[-1] in ['=', 'x']: new_w1_codes.append(c[:-1] + '-x')
                        elif c[-1] == '-': new_w1_codes.append(c[:-1] + 'x')
                line_word_codes[i-1] = list(set(line_word_codes[i-1] + new_w1_codes))
                line_word_codes[i] = list(set(line_word_codes[i] + [""])) # Waw is wiped
                
            # D. Word Grafting
            if w2_clean and w2_clean[0] in ['ا', 'آ'] and not heuristics.is_vowel_plus_h(w1_clean[-1]):
                new_w1_codes = []
                for c in line_word_codes[i-1]:
                    if not c: continue
                    if c[-1] == '=': new_w1_codes.append(c[:-1] + '-')
                    elif c[-1] == '-': new_w1_codes.append(c[:-1])
                line_word_codes[i-1] = list(set(line_word_codes[i-1] + new_w1_codes))
                
        return line_word_codes

    def scan_line(self, line):
        line_word_codes = self.get_line_word_codes(line)

        # Reverting to Sliding Syllable DP algorithm we implemented previously
        best_match, best_path, min_dist = None, "", float('inf')
        
        for idx, meter in enumerate(Meters.meters):
            # Try 4 variants like C# (Standard, Zi-aaf types)
            variants = []
            m_raw = meter.replace("/", "")
            variants.append(m_raw.replace("+", "")) # Meter 1
            variants.append(m_raw.replace("+", "") + "~") # Meter 2
            variants.append(m_raw.replace("+", "~") + "~") # Meter 3
            variants.append(m_raw.replace("+", "~")) # Meter 4
            
            for target in variants:
                res_path, res_dist = self._fuzzy_dp_match(line_word_codes, target)
                if res_dist < min_dist:
                    min_dist = res_dist
                    best_match = Meters.meter_names[idx]
                    best_path = res_path
                
                if res_dist == 0: return f"Perfect Match Found: {Meters.meter_names[idx]} [{res_path}]"

        # Special Matra-based meters
        for idx, meter in enumerate(Meters.special_meters):
            m_raw = meter.replace("/", "").replace("+", "")
            res_path, res_dist = self._fuzzy_dp_match(line_word_codes, m_raw)
            if res_dist == 0:
                m = self.calculate_matras(res_path)
                for j, t in enumerate([30, 22, 32, 14, 16, 12, 24, 8, 30, 22, 14]):
                    if m == t: return f"Perfect Match Found: {Meters.special_meter_names[j]} [{res_path}]"

        if best_match: return f"Match: {best_match} (Error: {min_dist} edits) [{best_path}]"
        return "Meter Not Found."

    def scan_poem(self, text):
        import math
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        if not lines: return ""
        results = []
        meter_line_scores = {} # {meter_name: [list of scores]}
        
        # 1. Find candidate meter NAMES from the first line to optimize speed
        first_line_word_codes = self.get_line_word_codes(lines[0])
        candidate_names = set()
        for idx, meter in enumerate(Meters.meters):
            m_raw = meter.replace("/", "").replace("+", "")
            _, dist, _ = self._fuzzy_dp_match(first_line_word_codes, m_raw)
            if dist <= 5: # Candidate must be reasonably close
                candidate_names.add(Meters.meter_names[idx])
        
        # 2. Gather scores for candidate meters across all lines
        for m_name in candidate_names: meter_line_scores[m_name] = []
        
        # Build a lookup for name to all its m_raw variants
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
                    if dist < best_dist_for_name:
                        best_dist_for_name = dist
                meter_line_scores[m_name].append(best_dist_for_name)
        
        # 2. Geometric Mean Ranking (Log/Exp formula)
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
            
            final_score = math.exp(score / count) - subtract
            if final_score < min_final_score:
                min_final_score = final_score
                best_overall_meter = m_name
        
        # 3. Output results using dominant meter
        for line in lines:
            results.append(f"{best_overall_meter}\n{line}\n{self.scan_line_against_meter(line, best_overall_meter)}")
        return "\n\n".join(results)

    def scan_line_against_meter(self, line, meter_name):
        words = line.split()
        line_word_codes = self.get_line_word_codes(line)
        
        best_path = ""
        best_dist = float('inf')
        
        # Check standard meters
        for idx, m_name in enumerate(Meters.meter_names):
            if m_name == meter_name:
                target = Meters.meters[idx].replace("/", "").replace("+", "")
                path, dist, _ = self._fuzzy_dp_match(line_word_codes, target)
                if dist < best_dist:
                    best_dist = dist
                    best_path = path
                    
        # Check special meters
        for idx, m_name in enumerate(Meters.special_meter_names):
            if m_name == meter_name:
                target = Meters.special_meters[idx].replace("/", "").replace("+", "")
                path, dist, _ = self._fuzzy_dp_match(line_word_codes, target)
                if dist < best_dist:
                    best_dist = dist
                    best_path = path
                    
        return f"[{best_path}] (Distance: {best_dist})"

    def _fuzzy_dp_match(self, word_codes, target):
        dp = [{} for _ in range(len(word_codes) + 1)]
        dp[0][0] = (0, "", [])
        for i in range(len(word_codes)):
            for pos, (d, path, code_list) in dp[i].items():
                for code in word_codes[i]:
                    new_pos = pos + len(code)
                    if new_pos <= len(target) + 2:
                        sub = target[pos:new_pos]
                        ld = 0
                        for k in range(min(len(code), len(sub))):
                            if sub[k] == '~' and code[k] == '-': ld += 0
                            elif code[k] != 'x' and code[k] != sub[k]: ld += 1
                        ld += abs(len(code) - len(sub))
                        if d + ld < dp[i+1].get(new_pos, (float('inf'), "", []))[0]:
                            dp[i+1][new_pos] = (d + ld, path + code, code_list + [code])
        best_p, best_d, best_list = "", float('inf'), []
        for pos, (d, path, code_list) in dp[len(word_codes)].items():
            final_d = d + abs(pos - len(target))
            if final_d < best_d: 
                best_d, best_p, best_list = final_d, path, code_list
        return best_p, best_d, best_list

    def calculate_matras(self, code):
        count = 0
        for c in code:
            if c == '-': count += 1
            elif c in ['=', 'x']: count += 2
        return count
