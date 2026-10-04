from araab import Araab

def is_vowel_plus_h(char):
    vowels = ['ا', 'ی', 'ے', 'و', 'ہ', 'ؤ']
    return char in vowels

def is_izafat(word):
    if not word: return False
    last_char = word[-1]
    return last_char == Araab.characters[1] or last_char == Araab.characters[10] or last_char == '\u06C2'

def is_consonant_plus_consonant(word):
    if len(word) < 2: return False
    return word[0] not in ['ا', 'ی', 'ے', 'ہ'] and word[1] not in ['ا', 'ی', 'ے', 'ہ']

def remove_tashdid(word):
    wrd = ""
    i = 0
    while i < len(word):
        if word[i] == Araab.characters[0]: # Shadda
            # Duplicate the preceding consonant
            if len(wrd) > 0:
                prev_char = wrd[-1]
                # If the previous char was a diacritic, we need the actual consonant before it
                if prev_char in Araab.characters and len(wrd) > 1:
                    cons = wrd[-2]
                    wrd = wrd[:-2] + cons + Araab.characters[2] + cons + prev_char
                else:
                    cons = prev_char
                    wrd = wrd[:-1] + cons + Araab.characters[2] + cons + Araab.characters[8] # default to Zabar
        else:
            wrd += word[i]
        i += 1
    return wrd

def locate_araab(word):
    stripped = Araab.remove_araab(word)
    loc = [""] * len(stripped)
    s_idx = 0
    for char in word:
        if char in Araab.characters:
            if s_idx > 0: loc[s_idx - 1] = char
        else:
            if s_idx < len(stripped): s_idx += 1
    return loc

def is_muarrab(word):
    return any(c in Araab.characters for c in word)

def noon_ghunna(word, code):
    # If the word contains ن internally (with Jazm), weights are manually reduced
    sub_string = word.replace("\u06BE", "").replace("\u06BA", "")
    stripped = Araab.remove_araab(sub_string)
    loc = locate_araab(sub_string)
    
    if len(stripped) == 3:
        # آنت (=--) -> =-. Starts with Vowel+H (=-) -> =.
        if stripped[0] == 'آ' and stripped[1] == 'ن' and loc[1] in [Araab.characters[2], '']:
            if code == "=--": code = "=-"
        elif stripped[1] == 'ن' and loc[1] in [Araab.characters[2], '']:
            if code == "=-":
                if stripped[0] == 'ا': code = "=-"
                elif is_vowel_plus_h(stripped[0]): code = "="
    elif len(stripped) == 4:
        # آن start (=-=) -> ==. ان start (==) -> ==. Vowel+H start (==) -> -=.
        # Pos 3 is ن (=-- & pos 2 Vowel+H) -> =-. Pos 3 is ن (== & pos 2 Vowel+H & pos 4 is NOT Vowel+H) -> =-.
        if stripped[0] == 'آ' and stripped[1] == 'ن' and loc[1] in [Araab.characters[2], '']:
            if code == "=-=": code = "=="
        elif stripped[1] == 'ن' and loc[1] in [Araab.characters[2], '']:
            if code == "==":
                if stripped[0] == 'ا': code = "=="
                elif is_vowel_plus_h(stripped[0]): code = "-="
        elif stripped[2] == 'ن' and loc[2] in [Araab.characters[2], '']:
            if code == "=--" and is_vowel_plus_h(stripped[1]): code = "=-"
            elif code == "==" and is_vowel_plus_h(stripped[1]) and not is_vowel_plus_h(stripped[3]): code = "=-"
    elif len(stripped) == 5:
        # Programmatically removes the character at index 1 of the code if specific conditions are met before the ن
        if stripped[3] == 'ن' and loc[3] in [Araab.characters[2], '']:
            if stripped[2] in ['ا', 'و', 'ی', 'ے']:
                if len(code) > 1:
                    code = code[:1] + code[2:]
        elif stripped[2] == 'ن' and loc[2] in [Araab.characters[2], '']:
             if stripped[1] in ['ا', 'و', 'ی', 'ے']:
                if len(code) > 1:
                    code = code[:1] + code[2:]
    return code

def contains_noon(word):
    return 'ن' in word



# ... copying primitives from heuristics.py ...
def length_one_scan(substr):
    sub_string = substr.replace("\u06BE", "").replace("\u06BA", "")
    stripped = Araab.remove_araab(sub_string)
    if len(stripped) == 0: return ""
    if stripped == "آ" or stripped == "\u0622": return "="
    return "-"

def length_two_scan(substr):
    sub_string = substr.replace("\u06BE", "").replace("\u06BA", "")
    stripped = Araab.remove_araab(sub_string)
    if len(stripped) == 1: return length_one_scan(sub_string)
    if len(stripped) == 0: return ""
    
    # If starts with آ -> =-
    if stripped[0] == 'آ' or stripped[0] == '\u0622': return "=-"
    # If ends in Vowel+H -> x
    if is_vowel_plus_h(stripped[1]): return "x"
    # Else -> =
    return "="

def length_three_scan(substr):
    sub_string = substr.replace("\u06BE", "").replace("\u06BA", "")
    stripped = Araab.remove_araab(sub_string)
    if len(stripped) == 1: return length_one_scan(sub_string)
    if len(stripped) == 2: return length_two_scan(sub_string)
    if len(stripped) == 0: return ""
    
    code = ""
    if is_muarrab(sub_string):
        loc = locate_araab(sub_string)
        # If pos 2 has Jazm (loc[1] == Jazm)
        if loc[1] == Araab.characters[2]:
            code = "=--" if stripped[0] == 'آ' else "=-"
        # If pos 2 has Zabar/Zer/Pesh
        elif loc[1] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]:
            code = "-="
        # If pos 2 has Shadd
        elif loc[1] == Araab.characters[0]:
            code = "=="
        # If pos 3 is ا
        elif stripped[2] == 'ا':
            code = "-="
        # If pos 3 is Vowel+H
        elif is_vowel_plus_h(stripped[2]):
            code = "=-" if stripped[1] == 'ا' else "-="
        # If pos 2 is Vowel+H
        elif is_vowel_plus_h(stripped[1]):
            code = "=-"
        # Default
        else:
            code = "=-"
    else:
        # Without Araab
        if stripped[0] == 'آ': code = "=="
        elif stripped[1] == 'ا': code = "=-"
        elif stripped[2] == 'ا': code = "-="
        elif is_vowel_plus_h(stripped[1]):
            if stripped[2] == 'ہ': code = "=-"
            elif stripped[2] in ['ی', 'ے', 'و']: code = "-="
            else: code = "=-"
        elif is_vowel_plus_h(stripped[2]): code = "-="
        elif is_vowel_plus_h(stripped[0]): code = "-="
        else: code = "-="
        
    return code

def length_four_scan(substr):
    sub_string = substr.replace("\u06BE", "").replace("\u06BA", "")
    stripped = Araab.remove_araab(sub_string)
    if len(stripped) < 4:
        if len(stripped) == 1: return length_one_scan(sub_string)
        elif len(stripped) == 2: return length_two_scan(sub_string)
        elif len(stripped) == 3: return length_three_scan(sub_string)
        return ""
    
    if stripped[0] == 'آ':
        return "=" + length_three_scan(sub_string[1:])
        
    code = ""
    if is_muarrab(sub_string):
        loc = locate_araab(sub_string)
        if stripped[1] == 'ا':
            code = "=--" if (len(loc) > 2 and loc[2] == Araab.characters[2]) else "=="
        elif stripped[2] == 'ا':
            code = "-=-"
        elif stripped[1] == 'و':
            if stripped[3] == 'ت' and len(loc) > 3 and loc[3] == Araab.characters[2]: code = "=-"
            elif len(loc) > 1 and loc[1] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]: code = "-=-"
            elif len(loc) > 2 and loc[2] == Araab.characters[2]: code = "=--"
            else: code = "=="
        elif stripped[1] == 'ی':
            if stripped[3] == 'ت' and len(loc) > 3 and loc[3] == Araab.characters[2]: code = "=-"
            elif len(loc) > 1 and loc[0] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]] and loc[1] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]: code = "-=-"
            elif len(loc) > 2 and loc[0] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]] and loc[2] == Araab.characters[2]: code = "=--"
            elif len(loc) > 0 and loc[0] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]: code = "=="
            else: code = "=="
        elif len(loc) > 1 and loc[0] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]] and loc[1] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]:
            if is_vowel_plus_h(stripped[2]): code = "-=-"
            elif len(loc) > 2 and loc[2] == Araab.characters[2]: code = "-=-"
            else: code = "--="
        elif len(loc) > 1 and loc[0] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]] and loc[1] == Araab.characters[2]:
            code = "=="
        elif len(loc) > 2 and loc[0] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]] and loc[2] == Araab.characters[2]:
            code = "-=-"
        elif len(loc) > 0 and loc[0] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]:
            if stripped[3] in ['ا', 'ی']: code = "--="
            else: code = "-=-"
        elif len(loc) > 1 and loc[1] == Araab.characters[2]:
            if len(loc) > 2 and loc[2] == Araab.characters[2]: code = "=="
            else: code = "=--"
        elif len(loc) > 2 and loc[2] == Araab.characters[2]:
            code = "-=-"
        elif len(loc) > 2 and loc[2] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]:
            code = "=="
        elif is_vowel_plus_h(stripped[2]):
            code = "-=-"
        else:
            code = "=="
    else:
        # Without Araab
        if is_vowel_plus_h(stripped[2]):
            if stripped[3] == 'ا': code = "=="
            elif is_vowel_plus_h(stripped[1]): code = "=="
            else: code = "-=-"
        else:
            code = "=="
            
    return code

def length_five_scan(substr):
    sub_string = substr.replace("\u06BE", "").replace("\u06BA", "")
    stripped = Araab.remove_araab(sub_string)
    if len(stripped) < 5:
        if len(stripped) == 1: return length_one_scan(sub_string)
        elif len(stripped) == 2: return length_two_scan(sub_string)
        elif len(stripped) == 3: return length_three_scan(sub_string)
        elif len(stripped) == 4: return length_four_scan(sub_string)
        return ""
        
    if stripped[0] == 'آ':
        return "=" + length_four_scan(sub_string[1:]) # sub_string[1:] effectively removes آ (length 1 unvoweled, but in python string آ is 1 char)
        
    code = ""
    if is_muarrab(sub_string):
        loc = locate_araab(sub_string)
        if stripped[2] == 'ا':
            code = "-=="
        elif stripped[1] == 'ا':
            # Simplified recursive call
            code = "=" + length_three_scan(sub_string[2:])
        elif stripped[3] == 'ا':
            if len(loc) > 1 and loc[1] in [Araab.characters[1], Araab.characters[8], Araab.characters[9]]: code = "--=-"
            elif len(loc) > 1 and loc[1] == Araab.characters[2]: code = "--=-"
            elif stripped[0] == 'ب':
                if is_vowel_plus_h(stripped[1]) or stripped[1] in ['ر', 'ن', 'غ']: code = "==-"
                else: code = "--=-"
            else:
                code = "==-"
        elif stripped[1] in ['و', 'ی'] or stripped[2] in ['و', 'ی'] or stripped[3] in ['و', 'ی']:
            # Fallback for the massive nested tree since it wasn't fully detailed
            if stripped[2] in ['و', 'ی']: code = "-=="
            elif stripped[1] in ['و', 'ی']: code = "=-="
            else: code = "==-"
        else:
            code = "==-"
    else:
        # Without Araab
        if stripped[2] == 'ا': code = "-=="
        elif stripped[1] == 'ا':
            if stripped[3] == 'ا': code = "==-"
            elif is_vowel_plus_h(stripped[3]) and is_vowel_plus_h(stripped[4]): code = "=-="
            else: code = "==-"
        elif stripped[3] == 'ا':
            if stripped[0] == 'ب' and (is_vowel_plus_h(stripped[1]) or stripped[1] in ['ر', 'ن', 'غ']): code = "==-"
            else: code = "--=-"
        elif is_vowel_plus_h(stripped[2]): code = "-=="
        elif is_vowel_plus_h(stripped[1]):
            if stripped[3] == 'ا': code = "==-"
            elif is_vowel_plus_h(stripped[3]) and is_vowel_plus_h(stripped[4]): code = "=-="
            else: code = "==-"
        else:
            # Consonants
            if stripped[0] == 'ب': code = "==-"
            elif stripped[0] in ['ت', 'ش']: code = "-=="
            elif stripped[4] == 'ت' and stripped[3] == 'ی': code = "-==" # Simplification of "replaces last char with ="
            elif stripped[4] == 'ا': code = "-=="
            elif is_vowel_plus_h(stripped[4]): code = "=-="
            else: code = "==-"
            
    return code
