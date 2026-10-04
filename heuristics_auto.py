from araab import Araab
from heuristics import *

def noon_ghunna(word, code:
        sub_= word.Replace("\u06BE", "").Replace("\u06BA", "") #/ remove ھ \u06BE and ں \u06BA for scansion purposes
        stripped = Araab.remove_araab(sub_string)
        loc = locate_araab(sub_string)
        if len(stripped) == 3:
            if stripped[0] == 'آ':
                if stripped[1] == 'ن' and loc[1] == Araab.characters[2]: #jazr
                    if code == "=--":  #آنت
                        code = "=-"
            elif stripped[1] == 'ن' and loc[1] == Araab.characters[2]:
                if code == "=-":
                    if stripped[0] == 'ا': #انگ
                        code = "=-"
                    elif is_vowel_plus_h(stripped[0]:  #ہنس
                        code = "="
        elif len(stripped) == 4:
            if stripped[0] == 'آ':
                if stripped[1] == 'ن' and loc[1] == Araab.characters[2]:
                    if code == "=-=":
                        code = "=="
            elif stripped[1] == 'ن' and loc[1] == Araab.characters[2]:
                if code == "==":
                    if stripped[0] == 'ا':   #اندر
                        code = "=="
                    elif is_vowel_plus_h(stripped[0]: #ہنسا
                        code = "-="
                elif code == "=--":
                    #find an example
            elif stripped[2] == 'ن' and loc[2] == Araab.characters[2]:
                if code == "=--":
                    if is_vowel_plus_h(stripped[1]: #باندھ،اونٹ، ہونٹ
                        code = "=-"
                elif code == "==":
                    if is_vowel_plus_h(stripped[1]: #بانگ
                        if not is_vowel_plus_h(stripped[3]:
                            code = "=-"
        elif len(stripped) == 5:
            if stripped[0] == 'آ':
                if stripped[1] == 'ن' and loc[1] == Araab.characters[2]:
                    if code[1] == '-':
                        code = code[:-1]
            elif stripped[1] == 'ن' and loc[1] == Araab.characters[2]:
                if code[0] == '=':
                    if stripped[0] == 'ا':   #انگیزی
                    elif is_vowel_plus_h(stripped[0]:
                    pass
                elif code == "=--":
                    #find an example
            elif stripped[2] == 'ن' and loc[2] == Araab.characters[2]:
                if code[0] == '=') and code[1] == '-':
                    if is_vowel_plus_h(stripped[1]:
                        code = code[:-1]
            elif stripped[3] == 'ن' and loc[3] == Araab.characters[2]:
                if code[len(code) - 1] == '-') and code[len(code) - 2] == '-':
                    if is_vowel_plus_h(stripped[2]:
                        if len(code) > 2:
                            if code[len(code) - 3] == '=':
                                code = code[:-1]
        return code
def length_one_scan(substr:
        code = ""
        if Araab.remove_araab(substr) == "\u0622": #/ \u0622 آ long syllable
            code = "="
        else:
            code = "-"
        return code
def length_two_scan(substr:
        #//////////////////////////// Two-lettered words /////////////////////////////////////////////
        #// Pritchett says: "...for by treating ALL one-syllable words of the forms given above
        #// as potentially flexible one never makes errors in ascertaining the meter of a poem." $2.1
        #// We are going to treat the two-lettered words ending in ا،ی،ے،و،ہ as flexible
        sub_= substr.Replace("\u06BE", "").Replace("\u06BA", "") #/ remove ھ \u06BE and ں \u06BA for scansion purposes
        stripped = Araab.remove_araab(sub_string)
        code = "="
        if substr[0] == '\u0622': # آ
        code = "=-"
        elif is_vowel_plus_h(stripped[len(stripped) - 1]:
        code = "x"
        return code
def length_three_scan(substr:
        code = ""
        sub_= substr.Replace("\u06BE", "").Replace("\u06BA", "") #/ remove ھ \u06BE and ں \u06BA for scansion purposes
        stripped = Araab.remove_araab(sub_string)
        if len(stripped) == 1:
            if stripped[0] == 'آ':
                return "-"
            else:
                return "="
        elif len(stripped) == 2:
            return length_two_scan(substr)
        if is_muarrab(sub_string:
            loc = locate_araab(sub_string)
            if loc[1] == Araab.characters[2]: #jazm
                if stripped[0] == 'آ':
                    code = "=--"
                else:
                    code = "=-"
            elif loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                code = "-="
            elif loc[1] == Araab.characters[0]: #shadd
                code = "=="
            elif stripped[2] == "ا":
                code = "-="
            elif stripped[2] == "ا") or stripped[2] == "ی") or stripped[2] == "ے") or stripped[2] == "و") or stripped[2] == "ہ": #vowels at end
                if stripped[1] == "ا":
                code = "=-"
                else:
                code = "-="
            elif stripped[1] == "ا") or stripped[1] == "ی") or stripped[1] == "ے") or stripped[1] == "و") or stripped[2] == "ہ": #vowels at center
                code = "=-"
            else: #default case
                code = "=-"
        else:
            if stripped[0] == 'آ':
                code = "=="
            elif stripped[1] == "ا": #Alif at centre
                code = "=-"
            elif stripped[2] == "ا":
                code = "-="
            elif stripped[1] == "ی") or stripped[1] == "ے") or stripped[1] == "و") or stripped[1] == "ہ": #vowels + h at centre
                if stripped[2] == "ہ":
                    code = "=-"
                elif stripped[2] == "ی") or stripped[2] == "ے") or stripped[2] == "و": #vowels + h at end
                    code = "-="
                else:
                    code = "=-"
            elif stripped[2] == "ی") or stripped[2] == "ے") or stripped[2] == "و") or stripped[2] == "ہ": #vowels + h at end
                code = "-="
            elif is_vowel_plus_h(stripped[0]:
                code = "-="
            else:
                code = "-="
        if contains_noon(stripped:
            code = NoonGhunna(substr, code)
        return code
def length_four_scan(substr:
        code = ""
        sub_= substr.Replace("\u06BE", "").Replace("\u06BA", "") #/ remove ھ \u06BE and ں \u06BA for scansion purposes
        stripped = Araab.remove_araab(sub_string)
        if len(stripped) == 1:
            code = length_one_scan(sub_string)
        elif len(stripped) == 2:
            code = length_two_scan(sub_string)
        elif len(stripped) == 3:
            code = length_three_scan(sub_string)
        else:
            if stripped[0] == 'آ':
                code = "=" + length_three_scan(sub_string[1:])
            elif is_muarrab(sub_string:
                loc = locate_araab(sub_string)
                if stripped[1] == 'ا':
                    if loc[2] == Araab.characters[2]: # jazr
                        code = "=--"
                    else:
                        code = "=="
                elif stripped[2] == 'ا':
                    code = "-=-"
                else:
                    if stripped[1] == 'و':
                        if stripped[3] == 'ت' and loc[3] == Araab.characters[2]: #jazm
                            code = "=-"
                        else:
                            if loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                                code = "-=-"
                            else:
                                if loc[2] == Araab.characters[2]: # jazr
                                    code = "=--"
                                else:
                                    code = "=="
                    elif stripped[1] == 'ی':
                        if stripped[3] == 'ت' and loc[3] == Araab.characters[2]: #jazm
                            code = "=-"
                        elif loc[0] == Araab.characters[1] or loc[0] == Araab.characters[8] or loc[0] == Araab.characters[9]: # zer, zabr, pesh
                            if loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                                code = "-=-"
                            else:
                                if loc[2] == Araab.characters[2]: #jazr
                                    code = "=--"
                                else:
                                    code = "=="
                        else:
                            code = "=="
                    else:
                        if loc[0] == Araab.characters[1] or loc[0] == Araab.characters[8] or loc[0] == Araab.characters[9]: # zer, zabr, pesh
                            if loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                                if is_vowel_plus_h(stripped[2]:
                                    code = "-=-"
                                elif loc[2] == Araab.characters[2]: # jazr
                                    code = "-=-"
                                else:
                                    code = "--="
                            elif loc[1] == Araab.characters[2]:
                                code = "=="
                            elif loc[2] == Araab.characters[2]:
                                code = "-=-"
                            else:
                                if stripped[3] == 'ا' or stripped[3] == 'ی':
                                    code = "--="
                                else:
                                    code = "-=-"
                        elif loc[1] == Araab.characters[2]:
                            if loc[2] == Araab.characters[2]:
                                code = "=="
                            else:
                                code = "=--"
                        elif loc[2] == Araab.characters[2]:
                            code = "-=-"
                        elif loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]: # zer, zabr, pesh
                            code = "=="
                        elif is_vowel_plus_h(stripped[2]:
                            code = "-=-"
                        else:
                            code = "=="
            elif is_vowel_plus_h(Araab.remove_araab(sub_string)[2]:
                if Araab.remove_araab(sub_string)[3] == 'ا':
                    code = "=="
                elif is_vowel_plus_h(Araab.remove_araab(sub_string)[1]:
                code = "=="
                else:
                code = "-=-"
            else: #default
                code = "=="
        if contains_noon(stripped:
            code = NoonGhunna(substr, code)
        return code
def length_five_scan(substr:
        code = ""
        sub_= substr.Replace("\u06BE", "").Replace("\u06BA", "") #/ remove ھ \u06BE and ں \u06BA for scansion purposes
        stripped = Araab.remove_araab(sub_string)
        if len(stripped) == 3:
            code = length_three_scan(substr)
        elif len(stripped) == 4:
            code = length_four_scan(substr)
        else:
            if stripped[0] == 'آ':
                code = "=" + length_four_scan(substr[2:])
            elif is_muarrab(substr:
                loc = locate_araab(substr)
                if stripped[1] == 'ا' or stripped[2] == 'ا' or stripped[3] == 'ا': # check alif at position 2,3,4
                    if stripped[2] == 'ا':
                        code = "-=="
                    elif stripped[1] == 'ا':
                        if is_muarrab(loc[0]:
                            if is_muarrab(loc[1]:
                                code = "=" + length_three_scan(substr[3:])
                            else:
                                code = "=" + length_three_scan(substr[4:])
                        else:
                            if is_muarrab(loc[1]:
                                code = "=" + length_three_scan(substr[2:])
                            else:
                                code = "=" + length_three_scan(substr[3:])
                    else:
                        code = "==-"
                        if loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                            code = "--=-"
                        elif loc[1] == Araab.characters[2]:
                            code = "--=-"
                        elif stripped[0] == 'ب':
                            if is_vowel_plus_h(stripped[1]:
                                code = "==-"
                            elif stripped[1] == 'ر':
                                code = "==-"
                            elif stripped[1] == 'ن':
                                code = "==-"
                            elif stripped[1] == 'غ':
                                code = "==-"
                            else:
                                code = "--=-"
                else:
                    if stripped[1] == 'و' or stripped[2] == 'و' or stripped[3] == 'و' or stripped[1] == 'ی' or stripped[2] == 'ی' or stripped[3] == 'ی':
                        if stripped[1] == 'و' or stripped[1] == 'ی':
                            if (loc[1] == Araab.characters[2]:
                                if is_muarrab(loc[0]:
                                    if is_muarrab(loc[1]:
                                        code = "=" + length_three_scan(substr[5:])
                                    else:
                                        code = "=" + length_three_scan(substr[4:])
                                else:
                                    if is_muarrab(loc[1]:
                                        code = "=" + length_three_scan(substr[3:])
                                    else:
                                        code = "=" + length_three_scan(substr[4:])
                            elif loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                                if loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]: # zer, zabr, pesh
                                    code = "--=-"
                                else:
                                    code = "-=="
                            else:
                                if (loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]) # zer, zabr, pesh :
                                    if loc[3] == Araab.characters[1] or loc[3] == Araab.characters[8] or loc[3] == Araab.characters[9]: # zer, zabr, pesh
                                        code = "=-="
                                    elif loc[3] == Araab.characters[2]:
                                        code = "==-"
                                    else:
                                        code = "==-"
                                elif loc[2] == Araab.characters[2]:
                                    if loc[3] == Araab.characters[1] or loc[3] == Araab.characters[8] or loc[3] == Araab.characters[9]: # zer, zabr, pesh
                                        code = "=-="
                                    elif loc[3] == Araab.characters[2]:
                                        code = "=---"
                                    else:
                                        if is_muarrab(loc[2]:
                                            code = "=" + length_three_scan(substr[4:])
                                        else:
                                            code = "=" + length_three_scan(substr[3:])
                                else:
                                    code = "=" + length_three_scan(substr[2:])
                        elif stripped[2] == 'و' or stripped[2] == 'ی':
                            if loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]: # zer, zabr, pesh
                                if (loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                                    if loc[3] == Araab.characters[1] or loc[3] == Araab.characters[8] or loc[3] == Araab.characters[9]: # zer, zabr, pesh
                                        code = "-----"   #highly unlikely
                                    else:
                                        code = "--=-"
                            elif loc[2] == Araab.characters[2]:
                                code = "-=="
                            else:
                                code = "-=="
                        elif stripped[3] == 'و' or stripped[3] == 'ی':
                            if loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]: # zer, zabr, pesh
                                if (loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                                    if loc[3] == Araab.characters[1] or loc[3] == Araab.characters[8] or loc[3] == Araab.characters[9]: # zer, zabr, pesh
                                        code = "---="   #highly unlikely
                                    else:
                                        code = "--=-"
                            elif loc[2] == Araab.characters[2]:
                                code = "-=="
                            else:
                                code = "==-"
                        else:
                            if loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]: # zer, zabr, pesh
                                if (loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                                    if loc[3] == Araab.characters[1] or loc[3] == Araab.characters[8] or loc[3] == Araab.characters[9]: # zer, zabr, pesh
                                        code = "-----"   #highly unlikely
                                    else:
                                        code = "--=-"
                            elif loc[2] == Araab.characters[2]:
                                code = "-=="
                            else:
                                code = "==-"
                    else:
                        if loc[1] == Araab.characters[1] or loc[1] == Araab.characters[8] or loc[1] == Araab.characters[9]: # zer, zabr, pesh
                            if loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]: # zer, zabr, pesh
                                if stripped[4] == 'ا':
                                    code = "---="
                                else:
                                    code = "--=-"
                            elif loc[2] == Araab.characters[2]:
                                code = "-=="
                            else:
                                code = "-=="
                        elif loc[1] == Araab.characters[2]:
                            if is_muarrab(loc[0]:
                                code = "=" + length_three_scan(substr[4:])
                            else:
                                code = "=" + length_three_scan(substr[3:])
                        elif loc[2] == Araab.characters[1] or loc[2] == Araab.characters[8] or loc[2] == Araab.characters[9]: # zer, zabr, pesh
                            code = "=-="
                        else:
                pass
            elif stripped[1] == 'ا' or stripped[2] == 'ا' or stripped[3] == 'ا': # check alif at position 2,3,4
                if stripped[2] == 'ا':
                    code = "-=="
                elif stripped[1] == 'ا':
                    if stripped[3] == 'ا':
                        code = "==-"
                    else:
                        if is_vowel_plus_h(stripped[3]:
                            if is_vowel_plus_h(stripped[4]:
                                code = "=-="
                            else:
                                code = "==-"
                        elif is_vowel_plus_h(stripped[4]:
                            code = "=-="
                        else:
                            code = "==-"
                else:
                    code = "==-"
                    if stripped[0] == 'ب':
                        if is_vowel_plus_h(stripped[1]:
                            code = "==-"
                        elif stripped[1] == 'ر':
                            code = "==-"
                        elif stripped[1] == 'ن':
                            code = "==-"
                        elif stripped[1] == 'غ':
                            code = "==-"
                        else:
                            code = "--=-"
            elif is_vowel_plus_h(stripped[1]) or is_vowel_plus_h(stripped[2]) or is_vowel_plus_h(stripped[3]: # check vowels at position 2,3,4
                if is_vowel_plus_h(stripped[2]:
                    code = "-=="
                    if is_vowel_plus_h(stripped[3]:
                        code = "-=="
                elif is_vowel_plus_h(stripped[1]:
                    if is_vowel_plus_h(stripped[3]:
                        code = "==-"
                    else:
                        if is_vowel_plus_h(stripped[3]:
                            if is_vowel_plus_h(stripped[4]:
                                code = "=-="
                            else:
                                code = "==-"
                        elif is_vowel_plus_h(stripped[4]:
                            code = "=-="
                        else:
                            code = "==-"
                else:
                    code = "==-"
                    if stripped[0] == 'ب':
                        if is_vowel_plus_h(stripped[1]:
                            code = "==-"
                        elif stripped[1] == 'ر':
                            code = "==-"
                        elif stripped[1] == 'ن':
                            code = "==-"
                        elif stripped[1] == 'غ':
                            code = "==-"
                        else:
                            code = "--=-"
                    if stripped[4] == 'ت' and stripped[3] == 'ی':
                        code = code[:-1]
                        code += "="
            else: #consonants
                code = "==-"
                if stripped[0] == 'ب':
                    if is_vowel_plus_h(stripped[1]:
                        code = "==-"
                    elif stripped[1] == 'ر':
                        code = "==-"
                    elif stripped[1] == 'ن':
                        code = "==-"
                    elif stripped[1] == 'غ':
                        code = "==-"
                    else:
                        code = "--=-"
                if stripped[0] == 'ت' or stripped[0] == 'ش':
                    code = "-=="
                if stripped[4] == 'ت' and stripped[3] == 'ی':
                    code = code[:-1]
                    code += "="
                if stripped[4] == 'ا': #???
                    code = "-=="
                elif is_vowel_plus_h(stripped[4]:
                    code = "=-="
        if contains_noon(stripped:
            code = NoonGhunna(substr, code)
        return code
    public Words pluralForm(substr, int len)
        Words wrd = new Words()
        wrd.word = substr
        substr = Araab.remove_araab(substr)
        if substr[0] == 'ا' and substr[1] == 'ل':
            substr = substr[2:]
        form1 = "", form2 = ""
        form1 = substr.Remove(len(substr) - len, len)
        form2 = form1 + "نا"
        wrd.word = form1
        wrd = findWord(wrd)
        if wrd.id.Count == 0:
            wrd.word = form2
            wrd = findWord(wrd)
        return wrd
    public Words pluralFormNoonGhunna(substr)
        Words wrd = new Words()
        wrd.word = substr
        substr = Araab.remove_araab(substr)
        if substr[0] == 'ا' and substr[1] == 'ل':
            substr = substr[2:]
        wrd.word = substr
        wrd = findWord(wrd)
        return wrd
    public Words pluralFormAat(substr)
        Words wrd = new Words()
        wrd.word = substr
        form1 = "", form2 = "", form3 = "", form4 = "", form5 = ""
        substr = Araab.remove_araab(substr)
        if substr[0] == 'ا' and substr[1] == 'ل':
            substr = substr[2:]
        int length = len(substr)
        form1 = substr.Remove(len(substr) - 2, 2)   # تصورات
        form2 = form1 + "ہ" #نظریہ،کلیہ
        form3 = substr.Remove(len(substr) - 2, 1) # آیت،صفت
        form4 = substr.Remove(len(substr) - 3, 1)
        wrd.word = form1
        wrd = findWord(wrd)
        if wrd.id.Count == 0:
            wrd.word = form2
            wrd = findWord(wrd)
            if wrd.id.Count == 0:
                wrd.word = form3
                wrd = findWord(wrd)
                if wrd.id.Count == 0:
                    if substr[length - 1] == 'ت' and substr[length - 2] == 'ا' and substr[length - 3] == 'ی':
                        wrd.word = form4
                        wrd = findWord(wrd)
                        if wrd.id.Count == 0:
                            wrd.word = form5
                            wrd = findWord(wrd)
        return wrd
    public Words pluralFormAan(substr)
        Words wrd = new Words()
        wrd.word = substr
        form1 = "", form2 = "", form3 = "",form4 = ""
        substr = Araab.remove_araab(substr)
        if substr[0] == 'ا' and substr[1] == 'ل':
            substr = substr[2:]
        int length = len(substr)
        form1 = substr.Remove(len(substr) - 2, 2)   # لڑکیاں
        form2 = form1 + "ہ" #رستوں
        form3 = form1 + "ا" # سودوں
        form4 = form1 + "نا" # دکھاوں
        wrd.word = form1
        wrd = findWord(wrd)
        if wrd.id.Count == 0:
            wrd.word = form2
            wrd = findWord(wrd)
            if wrd.id.Count == 0:
                wrd.word = form3
                wrd = findWord(wrd)
                if wrd.id.Count == 0:
                    wrd.word = form4
                    wrd = findWord(wrd)
        return wrd
    public Words pluralFormYe(substr)
        Words wrd = new Words()
        wrd.word = substr
        form1 = "", form2 = ""
        substr = Araab.remove_araab(substr)
        if substr[0] == 'ا' and substr[1] == 'ل':
            substr = substr[2:]
        int length = len(substr)
        form1 = substr.Remove(len(substr) - 2, 2) + "نا"   # ستائے
        form2 = substr.Remove(len(substr) - 2, 2)          # استغنائے
        wrd.word = form1
        wrd = findWord(wrd)
        if wrd.id.Count == 0:
            wrd.word = form2
            wrd = findWord(wrd)
        return wrd
    public Words findWord(Words wrd)
        connectionString = TaqtiController.connectionString
        MySqlConnection myConn = new MySqlConnection(connectionString)
        myConn.Open()
        MySqlCommand cmd = new MySqlCommand(connectionString)
        cmd = myConn.CreateCommand()
        searchWord = Araab.remove_araab(wrd.word)  #Remove Araab if present
        cmd.CommandText = "select * from exceptions where word like @search"
        cmd.Parameters.AddWithValue("@search", searchWord)
        MySqlDataReader dataReader = cmd.ExecuteReader()
        if dataReader.HasRows: # look in exceptions table
            while (dataReader.Read()
                Words wd = new Words()
                taqti2 = "", taqti3 = ""
                wrd.id.Add(dataReader.GetInt32(0)*-1)
                wrd.code.Add(dataReader.GetString(2).Replace(" ", "")
                try
                    taqti2 = dataReader.GetString(3).Replace(" ", "")
                catch
                try
                    taqti3 = dataReader.GetString(4).Replace(" ", "")
                catch
                if not String.IsNullOrEmpty(taqti2) wrd.code.Add(taqti2:
                if not String.IsNullOrEmpty(taqti3) wrd.code.Add(taqti3:
            myConn.Close()
        else:
            myConn.Close()
            MySqlConnection myConn2 = new MySqlConnection(connectionString)
            myConn2.Open()
            MySqlCommand cmd2 = new MySqlCommand(connectionString)
            cmd2 = myConn2.CreateCommand()
            cmd2.CommandText = "select * from mastertable where word like @s or word like @s1 or word like @s2 or word like @s3  or word like @s4 or word like @s5 or word like @s6 or word like @s7 or word like @s8 or word like @s9 or word like @s10 or word like @s11 or word like @s12"
            cmd2.Parameters.AddWithValue("@s", searchWord)
            cmd2.Parameters.AddWithValue("@s1", searchWord + " 1")
            cmd2.Parameters.AddWithValue("@s2", searchWord + " 2")
            cmd2.Parameters.AddWithValue("@s3", searchWord + " 3")
            cmd2.Parameters.AddWithValue("@s4", searchWord + " 4")
            cmd2.Parameters.AddWithValue("@s5", searchWord + " 5")
            cmd2.Parameters.AddWithValue("@s6", searchWord + " 6")
            cmd2.Parameters.AddWithValue("@s7", searchWord + " 7")
            cmd2.Parameters.AddWithValue("@s8", searchWord + " 8")
            cmd2.Parameters.AddWithValue("@s9", searchWord + " 9")
            cmd2.Parameters.AddWithValue("@s10", searchWord + " 10")
            cmd2.Parameters.AddWithValue("@s11", searchWord + " 11")
            cmd2.Parameters.AddWithValue("@s12", searchWord + " 12")
            MySqlDataReader dataReader2 = cmd2.ExecuteReader()
            if dataReader2.HasRows: # found word in mastertable?
                while (dataReader2.Read()
                    Words wd = new Words()
                    wrd.id.Add(dataReader2.GetInt32(0)
                    wrd.muarrab.Add(dataReader2.GetString(2).Trim()
                    wrd.taqti.Add(dataReader2.GetString(3).Trim()
                    try
                        wrd.language.Add(dataReader2.GetString(4)
                    catch
                    wrd.isVaried.Add(dataReader2.GetBoolean(5)
                    wrd.code.Add(assignCode(wrd)
                myConn2.Close()
                if wrd.isVaried.Count > 0:
                    if wrd.isVaried[0]:
                        MySqlConnection con = new MySqlConnection(connectionString)
                        con.Open()
                        MySqlCommand cmdtemp = new MySqlCommand(connectionString)
                        cmdtemp = con.CreateCommand()
                        cmdtemp.CommandText = "select * from variations where id = @id"
                        cmdtemp.Parameters.AddWithValue("@id",wrd.id[0])
                        MySqlDataReader dR2 = cmdtemp.ExecuteReader()
                        if dR2.HasRows: # found word in mastertable?
                            while (dR2.Read()
                                Words wd = new Words()
                                wrd.id.Add(dR2.GetInt32(0)
                                wrd.muarrab.Add(dR2.GetString(2).Trim()
                                wrd.taqti.Add(dR2.GetString(3).Trim()
                                wrd.code.Add(assignCode(wrd)
                            con.Close()
                        con.Close()
            else: #else: search in plurals table
                myConn2.Close()
                MySqlConnection myConn3 = new MySqlConnection(connectionString)
                myConn3.Open()
                MySqlCommand cmd3 = new MySqlCommand(connectionString)
                cmd3 = myConn3.CreateCommand()
                cmd3.CommandText = "select * from Plurals where word like @s"
                cmd3.Parameters.AddWithValue("@s",searchWord)
                MySqlDataReader dataReader3 = cmd3.ExecuteReader()
                if dataReader3.HasRows:
                    while (dataReader3.Read()
                        Words wd = new Words()
                        wrd.id.Add(dataReader3.GetInt32(0)
                        wrd.muarrab.Add(dataReader3.GetString(2).Trim()
                        wrd.taqti.Add(dataReader3.GetString(3).Trim()
                        wrd.code.Add(assignCode(wrd)
                    myConn3.Close()
                else: # not found in plurals either? find in variations table
                    myConn3.Close()
                    MySqlConnection myConn4 = new MySqlConnection(connectionString)
                    myConn4.Open()
                    MySqlCommand cmd4 = new MySqlCommand(connectionString)
                    cmd4 = myConn4.CreateCommand()
                    cmd4.CommandText = "select * from Variations where word like @s"
                    cmd4.Parameters.AddWithValue("@s",searchWord)
                    MySqlDataReader dataReader4 = cmd4.ExecuteReader()
                    if dataReader4.HasRows:
                        while (dataReader4.Read()
                            Words wd = new Words()
                            wrd.id.Add(dataReader4.GetInt32(0)
                            wrd.muarrab.Add(dataReader4.GetString(2).Trim()
                            wrd.taqti.Add(dataReader4.GetString(3).Trim()
                            wrd.code.Add(assignCode(wrd)
                    myConn4.Close()
        myConn.Close()
        return wrd
    public Words wordCode(Words wrd)
        wrd = findWord(wrd)
        if wrd.id.Count > 0:
            sub_=   Araab.remove_araab(wrd.word.Replace("\u06BE", "").Replace("\u06BA", "") #/ remove ھ \u06BE and ں \u06BA for scansion purposes
            if sub_string.len == 3:
                if sub_string[2] == 'ا':
                    if sub_string[0] == 'آ':
                        if not wrd.code[0] == "==") and not wrd.code[0] == "=x":
                            wrd.id.Add(-1)
                            wrd.code.Add("==")
                    else:
                        if not wrd.code[0] == "-=") and not wrd.code[0] == "-x":
                            wrd.id.Add(-1)
                            wrd.code.Add("-=")
        if wrd.id.Count == 0: #word not found in dictionary
            code = ""
            int id = -1
            bool flag = True
            stripped = Araab.remove_araab(wrd.word)
            int length = len(stripped)
            wrd.modified = True
            Words wd
            #/////////////Noon Ghunna at the end (ں)  /////////////
            if len(stripped) > 3:
                if stripped[length - 1] == 'ں':
                    originalWord = wrd.word
                    wd = pluralForm(wrd.word.Remove(wrd.word.len - 1, 1) + "ن", 0)
                    if wd.id.Count > 0:
                        for (int k = 0 k < wd.code.Count k++)
                            if wd.code[k][wd.code[k].len - 1] == '-':
                                wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                        flag = False
                    if not flag:
                        wrd.id = wd.id
                        wrd.code = wd.code
                        wrd.isVaried = wd.isVaried
                        wrd.language = wd.language
                        wrd.length = wd.length
                        for (int k = 0 k < wd.muarrab.Count k++)
                            wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len-1) + "ں")
                        wrd.taqti = wd.taqti
                        wrd.taqtiWordGraft = wd.taqtiWordGraft
            if len(stripped) > 4:
                if stripped[length - 1] == 'ے' and stripped[length - 2] == 'ئ':
                    originalWord = wrd.word
                    wd = pluralForm(wrd.word, 2)
                    if wd.id.Count > 0:
                        form1 = "", form2 = ""
                        substr = Araab.remove_araab(wd.word)
                        int len = len(substr)
                        form1 = stripped.Remove(len(stripped) - 2, 2)
                        form2 = form1 + "نا"
                        if substr == form1:
                            for (int k = 0 k < wd.code.Count k++)
                                if wd.code[k][wd.code[k].len - 1] == 'x':
                                    wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                    wd.code[k] += "="
                                wd.code[k] += "x"
                            for (int k = 0 k < wd.muarrab.Count k++)
                                wrd.muarrab.Add(wd.muarrab[k] + "ئے")
                            flag = False
                        else: #no change required
                            for (int k = 0 k < wd.muarrab.Count k++)
                                wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len-2) + "ئے")
                            flag = False
                    if not flag:
                        wrd.id = wd.id
                        wrd.code = wd.code
                        wrd.isVaried = wd.isVaried
                        wrd.language = wd.language
                        wrd.length = wd.length
                        wrd.taqti = wd.taqti
                        wrd.taqtiWordGraft = wd.taqtiWordGraft
            #////////////// Plural Case ///////////////////////////
            if flag:
                if len(stripped) >= 4:
                    if stripped[length - 1] == 'ا' and stripped[length - 2] == 'ت':
                        wd = pluralForm(wrd.word, 2)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 2, 2)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "تا"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "تا")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "تا")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
                    elif stripped[length - 1] == 'ے' and stripped[length - 2] == 'ت':
                        wd = pluralForm(wrd.word, 2)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 2, 2)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "تے"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "تے")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "تے")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
                    elif stripped[length - 1] == 'ی' and stripped[length - 2] == 'ت':
                        wd = pluralForm(wrd.word, 2)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 2, 2)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "تی"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "تی")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "تی")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
                    elif stripped[length - 1] == 'ں' and stripped[length - 2] == 'ی' and stripped[length - 3] == 'ت':
                        wd = pluralForm(wrd.word, 3)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 3, 3)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "تیں"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "تیں")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "تیں")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.muarrab = wd.muarrab
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
            if flag:
                if len(stripped) > 4:
                    if stripped[length - 1] == 'ا' and stripped[length - 2] == 'ن':
                        wd = pluralForm(wrd.word, 2)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 2, 2)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "نا"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "نا")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "نا")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
                    elif stripped[length - 1] == 'ے' and stripped[length - 2] == 'ن':
                        wd = pluralForm(wrd.word, 2)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 2, 2)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "نے"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "نے")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "نے")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
                    elif stripped[length - 1] == 'ی' and stripped[length - 2] == 'ن':
                        wd = pluralForm(wrd.word, 2)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 2, 2)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "نی"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "نی")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "نی")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
                    elif stripped[length - 1] == 'ں' and stripped[length - 2] == 'ی' and stripped[length - 3] == 'ئ':
                        wd = pluralForm(wrd.word, 3)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 3, 3)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "ئیں"
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + "ئیں")
                                flag = False
                            else: #no change required
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + "ئیں")
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
            if flag:
                if len(stripped) > 4:
                    if stripped[length - 1] == 'ا' or stripped[length - 1] == 'ے' or stripped[length - 1] == 'ی' or stripped[length - 1] == 'و' or stripped[length - 1] == 'ہ' or stripped[length - 1] == 'ؤ':
                        wd = pluralForm(wrd.word, 1)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = stripped.Remove(len(stripped) - 1, 1)
                            form2 = form1 + "نا"
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k].len >= 2:
                                        if wd.code[k][wd.code[k].len - 1] == '-':
                                            wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                            wd.code[k] += "x"
                                        elif wd.code[k][wd.code[k].len - 1] == '=':
                                            if wd.code[k][wd.code[k].len - 2] == '-':
                                                wd.code[k] = wd.code[k].Remove(wd.code[k].len - 2, 2)
                                                wd.code[k] += "=x"
                                            else:
                                                wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                                wd.code[k] += "-x"
                                    else:
                                        wd.code[k] = wd.code[k][1:]
                                        wd.code[k] += "-x"
                                wd.word += stripped[length - 1]
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k] + stripped[length - 1])
                                flag = False
                            else:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k].len > 2:
                                        if wd.code[k][wd.code[k].len - 2] == '-':
                                            wd.code[k] = wd.code[k].Remove(wd.code[k].len - 2, 2)
                                            wd.code[k] += "x"
                                        elif wd.code[k][wd.code[k].len - 2] == '=':
                                            if wd.code[k][wd.code[k].len - 3] == '-':
                                                wd.code[k] = wd.code[k].Remove(wd.code[k].len - 3, 3)
                                                wd.code[k] += "=x"
                                            else:
                                                wd.code[k] = wd.code[k].Remove(wd.code[k].len - 2, 2)
                                                wd.code[k] += "-x"
                                    else:
                                        wd.code[k] = wd.code[k][2:]
                                        wd.code[k] += "-x"
                                wd.word += wd.word.Remove(wd.word.len-2) +  stripped[length - 1]
                                for (int k = 0 k < wd.muarrab.Count k++)
                                    wrd.muarrab.Add(wd.muarrab[k].Remove(wd.muarrab[k].len - 2) + stripped[length - 1])
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
            if flag:
                if len(stripped) > 4:
                    if (stripped[length - 1] == 'ت' and stripped[length - 2] == 'ا') or (stripped[length - 1] == 'ت' and stripped[length - 2] == 'ا' and stripped[length - 3] == 'ی':
                        originalWord = wrd.word
                        wd = pluralFormAat(wrd.word)
                        if wd.id.Count > 0:
                            for (int k = 0 k < wd.code.Count k++)
                                form1 = "", form2 = "", form3 = "", form4 = "", form5 = ""
                                substr
                                strpd = Araab.remove_araab(originalWord)
                                substr = Araab.remove_araab(wd.word)
                                int len = len(substr)
                                form1 = strpd.Remove(strpd.len - 2, 2)   # تصورات
                                form2 = form1 + "ہ" #نظریہ،کلیہ
                                form3 = strpd.Remove(strpd.len - 2, 1) # آیت،صفت
                                if Araab.remove_araab(originalWord)[len - 1] == 'ت' and Araab.remove_araab(originalWord)[len - 2] == 'ا' and Araab.remove_araab(originalWord)[len - 3] == 'ی':
                                    form4 = strpd.Remove(strpd.len - 3, 3)   # اخلاقیات
                                    form5 = form4 + "ہ"
                                    #مادیات
                                    if substr == form4:
                                        wd.code[k] += "=-"
                                        for (int l = 0 l < wd.muarrab.Count l++)
                                            wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len-3)
                                    elif substr == form5:
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "-=-"
                                        for (int l = 0 l < wd.muarrab.Count l++)
                                            wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 1)
                                if substr == form1:
                                    if wd.code[k][wd.code[k].len - 1] == "=") or wd.code[k][wd.code[k].len - 1] == "x":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "-=-"
                                    elif wd.code[k][wd.code[k].len - 1] == "-":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "=-"
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 2)
                                elif substr == form2:
                                    wd.code[k] = wd.code[k].Replace("x", "=") + "-"
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 1)
                                elif substr == form3:
                                    if wd.code[k][wd.code[k].len - 1] == "=") or wd.code[k][wd.code[k].len - 1] == "x":
                                        wd.code[k] = wd.code[k].Replace("x", "=") + "-"
                                    elif wd.code[k][wd.code[k].len - 1] == "-":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 2, 2)
                                        wd.code[k] += "-=-"
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 1)
                            flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            if (stripped[length - 1] == 'ت' and stripped[length - 2] == 'ا' and stripped[length - 3] == 'ی':
                                for (int l = 0 l < wrd.muarrab.Count l++)
                                    wrd.muarrab[l] = wrd.muarrab[l] + "یات"
                            elif stripped[length - 1] == 'ت' and stripped[length - 2] == 'ا':
                                for (int l = 0 l < wrd.muarrab.Count l++)
                                    wrd.muarrab[l] = wrd.muarrab[l] + "ات"
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
            if flag:
                if len(stripped) > 4:
                    if (stripped[length - 1] == 'ں' and stripped[length - 2] == 'ا') or (stripped[length - 1] == 'ں' and stripped[length - 2] == 'و') or (stripped[length - 1] == 'ں' and stripped[length - 2] == 'ی':
                        originalWord = wrd.word
                        wd = pluralFormAan(wrd.word)
                        if wd.id.Count > 0:
                            for (int k = 0 k < wd.code.Count k++)
                                form1 = "", form2 = "", form3 = "", form4 = ""
                                substr
                                strpd = Araab.remove_araab(originalWord)
                                substr = Araab.remove_araab(wd.word)
                                int len = len(substr)
                                form1 = strpd.Remove(strpd.len - 2, 2)   # لڑکیاں
                                form2 = form1 + "ہ" #رستوں
                                form3 = form1 + "ا" # سودوں
                                form4 = form1 + "نا" # دکھاوں
                                if substr == form1:
                                    if wd.code[k][wd.code[k].len - 1] == "=") or wd.code[k][wd.code[k].len - 1] == "x":
                                        if wd.code[k].len > 1:
                                            wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                            wd.code[k] += "-x"   # زادیوں
                                        else:
                                            wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                            wd.code[k] += "-x"
                                    elif wd.code[k][wd.code[k].len - 1] == "-":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "x"
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l] + stripped[length - 2] + stripped[length - 1])
                                elif substr == form2:
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 1) + stripped[length - 2] + stripped[length - 1])
                                    # no addition required  رتبوں، رستوں
                                elif substr == form3:
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 1) + stripped[length - 2] + stripped[length - 1])
                                    # no addition required
                                elif substr == form4:
                                    if wd.code[k][wd.code[k].len - 1] == "=") or wd.code[k][wd.code[k].len - 1] == "x":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "-"
                                    elif wd.code[k][wd.code[k].len - 1] == "-":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "-"
                                for (int l = 0 l < wd.muarrab.Count l++)
                                    wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 2) + stripped[length - 2] + stripped[length - 1])
                            flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
            if flag:
                if len(stripped) > 4:
                    if (stripped[length - 1] == 'ں' and stripped[length - 2] == 'ؤ':
                        originalWord = wrd.word
                        wd = pluralFormAan(wrd.word)
                        if wd.id.Count > 0:
                            for (int k = 0 k < wd.code.Count k++)
                                form1 = "", form2 = "", form3 = "", form4 = ""
                                substr
                                strpd = Araab.remove_araab(originalWord)
                                substr = Araab.remove_araab(wd.word)
                                int len = len(substr)
                                form1 = strpd.Remove(strpd.len - 2, 2)   # لڑکیاں
                                form2 = form1 + "ہ" #رستوں
                                form3 = form1 + "ا" # سودوں
                                form4 = form1 + "نا" # دکھاوں
                                if substr == form1:
                                    if wd.code[k][wd.code[k].len - 1] == "=") or wd.code[k][wd.code[k].len - 1] == "x":
                                        if wd.code[k].len > 1:
                                            wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                            wd.code[k] += "=x"
                                        else:
                                            wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                            wd.code[k] += "-x"
                                    elif wd.code[k][wd.code[k].len - 1] == "-":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "x"
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l] + stripped[length - 2] + stripped[length - 1])
                                elif substr == form2:
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 1) + stripped[length - 2] + stripped[length - 1])
                                    # no addition required  رتبوں، رستوں
                                elif substr == form3:
                                    for (int l = 0 l < wd.muarrab.Count l++)
                                        wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 1) + stripped[length - 2] + stripped[length - 1])
                                    # no addition required
                                elif substr == form4:
                                    if wd.code[k][wd.code[k].len - 1] == "=") or wd.code[k][wd.code[k].len - 1] == "x":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "x"
                                    elif wd.code[k][wd.code[k].len - 1] == "-":
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1)
                                        wd.code[k] += "x"
                                for (int l = 0 l < wd.muarrab.Count l++)
                                    wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 2) + stripped[length - 2] + stripped[length - 1])
                            flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
            if flag:
                if len(stripped) > 2:
                    if stripped[length - 1] == 'ا':
                        originalWord = wrd.word
                        wd = pluralForm(wrd.word, 0)
                        if wd.id.Count > 0:
                            for (int k = 0 k < wd.code.Count k++)
                                form1 = "", form2 = ""
                                substr
                                strpd = Araab.remove_araab(originalWord)
                                substr = Araab.remove_araab(wd.word)
                                int len = len(substr)
                                form1 = strpd
                                form2 = form1 + "نا"
                                if substr == form1:
                                    pass
                                elif substr == form2:
                                    if wd.code[k][wd.code[k].len - 2] == '=':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 2, 2)
                                        wd.code[k] += "x"
                                    else:
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 2, 2)
                                        wd.code[k] += "-"
                            flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.muarrab = wd.muarrab
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
            if flag:
                if (stripped[length - 1] == 'ن' and stripped[length - 2] == 'ا':
                if len(stripped) > 2:
                    originalWord = wrd.word
                    wd = pluralFormPostfixAan(wrd.word)
                    if wd.id.Count > 0:
                        for (int k = 0 k < wd.code.Count k++)
                            if wd.code[k][wd.code[k].len - 1] == '-':
                                wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                wd.code[k] += "=-"
                            else:
                                wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                wd.code[k] += "-=-"
                        for (int l = 0 l < wd.muarrab.Count l++)
                            wrd.muarrab.Add(wd.muarrab[l] + "ان")
                        flag = False
                    if not flag:
                        wrd.id = wd.id
                        wrd.code = wd.code
                        wrd.isVaried = wd.isVaried
                        wrd.language = wd.language
                        wrd.length = wd.length
                        wrd.taqti = wd.taqti
                        wrd.taqtiWordGraft = wd.taqtiWordGraft
            #/////////////////Special cases/////////////////////////
            if flag:
                if len(stripped) > 4:
                    if (stripped[length - 1] == 'ی' and stripped[length - 2] == 'ئ') | (stripped[length - 1] == 'ے' and stripped[length - 2] == 'ئ') or (stripped[length - 1] == 'ی' and stripped[length - 2] == 'ت') or (stripped[length - 1] == 'ا' and stripped[length - 2] == 'ت') or (stripped[length - 1] == 'ے' and stripped[length - 2] == 'ت') or (stripped[length - 1] == 'ے' and stripped[length - 2] == 'ن':
                        originalWord = wrd.word
                        wd = pluralFormYe(wrd.word)
                        if wd.id.Count > 0:
                            form1 = "", form2 = ""
                            substr
                            strpd = Araab.remove_araab(originalWord)
                            substr = Araab.remove_araab(wd.word)
                            int len = len(substr)
                            form1 = strpd.Remove(strpd.len - 2, 2)
                            form2 = form1 + "نا" #رستوں
                            if substr == form1:
                                for (int k = 0 k < wd.code.Count k++)
                                    if wd.code[k][wd.code[k].len - 1] == 'x':
                                        wd.code[k] = wd.code[k].Remove(wd.code[k].len - 1, 1)
                                        wd.code[k] += "="
                                    wd.code[k] += "x"
                                wd.word += "تا"
                                for (int l = 0 l < wd.muarrab.Count l++)
                                    wrd.muarrab.Add(wd.muarrab[l] + stripped[length - 2] + stripped[length - 1])
                                flag = False
                            else:
                                for (int l = 0 l < wd.muarrab.Count l++)
                                    wrd.muarrab.Add(wd.muarrab[l].Remove(wd.muarrab[l].len - 2) + stripped[length - 2] + stripped[length - 1])
                                flag = False
                        if not flag:
                            wrd.id = wd.id
                            wrd.code = wd.code
                            wrd.isVaried = wd.isVaried
                            wrd.language = wd.language
                            wrd.length = wd.length
                            wrd.taqti = wd.taqti
                            wrd.taqtiWordGraft = wd.taqtiWordGraft
                        if len(stripped) == 4:
                            if is_vowel_plus_h(stripped[1]:
                                code = "=x"
                            else:
                                code = "=x"
                            flag = False
                        /* else:
                            if stripped[0] == 'آ':
                                code = "=x"
                            else:
                                code = "=x"
                            flag = False
                            }*/
                            /*if not flag:
                                wrd.id.Add(-1)
                                wrd.code.Add(code)
                                wrd.length = Araab.remove_araab(wrd.word).len
                                }*/
                    if flag:
                        if len(stripped) > 1:
                            if stripped[0] == 'ا' and stripped[1] == 'ل':
                                wd = pluralForm(wrd.word, 0)
                                if wd.id.Count > 0:
                                    for (int k = 0 k < wd.code.Count k++)
                                        wd.code[k] = "=" + wd.code[k]
                                    flag = False
                                if not flag:
                                    wrd.id = wd.id
                                    wrd.code = wd.code
                                    wrd.isVaried = wd.isVaried
                                    wrd.language = wd.language
                                    wrd.length = wd.length
                                    wrd.muarrab = wd.muarrab
                                    wrd.taqti = wd.taqti
                                    wrd.taqtiWordGraft = wd.taqtiWordGraft
                    if wrd.id.Count > 0:
                        word = Araab.remove_araab(wrd.word.Replace("ں", "")
                        if is_vowel_plus_h(word[word.len-1]:
                            for (int k = 0 k < wrd.code.Count k++)
                                if wrd.code[k][wrd.code[k].len - 1] == "=":   # Word-end flexible syllable
                                    if Araab.remove_araab(word)[word.len - 1] == 'ا' or Araab.remove_araab(word)[word.len - 1] == 'ی' :
                                        if wrd.language.Count > 0:
                                            bool fl = False
                                            for (int x = 0 x < wrd.language.Count x++)
                                                if wrd.language[x] == "عربی") and not wrd.modified:
                                                    fl = True
                                                elif wrd.language[x] == "فارسی") and Araab.remove_araab(word)[word.len - 1] == 'ا' and not wrd.modified:
                                                    fl = True
                                            if fl:
                                                wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1, 1)
                                                wrd.code[k] += "="
                                            else:
                                                wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1, 1)
                                                wrd.code[k] += "x"
                                        else:
                                            wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1, 1)
                                            wrd.code[k] += "x"
                                    else:
                                        wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1, 1)
                                        wrd.code[k] += "x"
                return wrd
            public bool contains_noon(word)
                if word.len > 1:
                    for(int i = 0 i < word.len-1 i++)
                        if word[i] == 'ن':
                            return True
                else:
                    return False
                return False
            public Words pluralFormPostfixAan(substr)
                Words wrd = new Words()
                wrd.word = substr
                form1 = ""
                substr = Araab.remove_araab(substr)
                if substr[0] == 'ا' and substr[1] == 'ل':
                    substr = substr[2:]
                int length = len(substr)
                form1 = substr.Remove(len(substr) - 2, 2)
                wrd.word = form1
                wrd = findWord(wrd)
                return wrd
            public Words compoundWord(Words wrd)
                Words wd = new Words()
                wd.word = wrd.word
                stripped = Araab.remove_araab(wrd.word)
                for (int i = 1 i < len(stripped) - 1 i++)
                    bool flag = False
                    Words first = new Words()
                    first.word = stripped.Substring(0, i)
                    first = findWord(first)
                    Words second = new Words()
                    second.word = stripped.Substring(i, len(stripped) - i)
                    second = wordCode(second)
                    if first.id.Count > 0:
                        if second.id.Count == 0:
                            if second.word.len <= 2:
                                second.code.Add(length_two_scan(second.word)
                                second.id.Add(-1)
                                flag = True
                        else:  #perfectonot not not 
                            flag = True
                    else:
                        if second.id.Count > 0:
                            if first.word.len <= 2:
                                first.code.Add(length_two_scan(first.word)
                                first.id.Add(-1)
                                flag = True
                    if flag:
                        first.word += "" + second.word
                        List<string> codes = new List<string>()
                        for (int k = 0 k < first.code.Count k++)
                            for (int j = 0 j < second.code.Count j++)
                                codes.Add(first.code[k] + second.code[j])
                        first.code = codes
                        List<string> muarrab = new List<string>()
                        for (int k = 0 k < first.muarrab.Count k++)
                            for (int j = 0 j < second.muarrab.Count j++)
                                muarrab.Add(first.muarrab[k] + second.muarrab[j])
                        first.muarrab = muarrab
                        wd = first
                        break
                wd.modified = True
                return wd
            static public removeTashdid(word)
                wrd = ""
                if is_muarrab(word:
                    for (int i = 0 i < word.len i++)
                        if word[i] == Araab.characters[0]: #shadd
                            if i - 2 > -1:
                                if not is_muarrab(word[i - 2]:
                                    if not is_muarrab(word[i - 1]:
                                        wrd = wrd.Remove(wrd.len - 1)
                                        wrd += word[i - 1] + Araab.characters[2] + word[i - 1] + Araab.characters[8]
                                    else:
                                        wrd = wrd.Remove(wrd.len - 2)
                                        wrd += word[i - 2] + Araab.characters[2] + word[i - 2] + Araab.characters[8]
                                else:
                                    wrd += Araab.characters[2] + word[i - 1] + Araab.characters[8]
                            else:
                                wrd += Araab.characters[2] + word[i - 1] + Araab.characters[8]
                        else:
                            wrd += word[i]
                    return wrd
                else:
                return word
            public zamzamaFeet(int index,code)
                feet = ""
                int len = 0
                if code[len(code) - 1] == '-':
                    code = code.Remove(len(code) - 1)
                    len = len(code)
                else:
                    len = len(code)
                for (int i = 0 i < len i++)
                    if code[i] == '-':
                        if i < len(code):
                            if code[++i] == '-':
                                if i < len(code):
                                    if code[++i] == '=':
                                        feet += " فَعِلن"
                                else:
                                    break
                        else:
                            break
                    else:
                        if i < len(code):
                            if code[++i] == '=':
                                feet += " فعْلن"
                        else:
                            break
                return feet
            public hindiFeet(int ind, code)
                feet = ""
                int len = 0
                string[] afail = { "==","=-","-==","-=-","-=","=","==-","-==-"}
                string[] names = { "فعلن", "فعْل", "فعولن", "فعول", "فَعَل", "فع", "فعْلان", "فعولان"}
                int numFeet = 0
                if ind == 0 or ind == 1 or ind == 3 or ind == 2 or ind == 4 or ind == 5 or ind == 6 or ind == 7:
                    if code[len(code)-1] == '-':
                        code = code.Remove(len(code) - 1)
                        len = len(code)
                    else:
                        len = len(code)
                    if len > 0:
                        for (int j = 0 j < len j++)
                            int index = -1
                            for (int k = 0 k < afail.Count() k++)
                                bool flag = True
                                index = k
                                if j + afail[k].len > len(code):
                                    index = -1
                                    flag = False
                                else:
                                    slice = code.Substring(j, afail[k].len)
                                    for (int z = 0 z < afail[k].len z++)
                                        if not ((slice[z] == afail[k][z]) :
                                            flag = False
                                            index = -1
                                            break
                                if flag:
                                break
                            if index >= 0:
                                j = j + afail[index].len - 1
                                feet += names[index] + " "
                                numFeet++
                            else:
                                break
                    else:
                    return feet
                if ind == 0 and numFeet == 8:
                    return feet
                elif ind == 1 and numFeet == 6:
                    return feet
                elif ind == 2 and numFeet == 8:
                    return feet
                elif ind == 3 and numFeet == 4:
                    return feet
                elif ind == 4 and numFeet == 4:
                    return feet
                elif ind == 5 and numFeet == 3:
                    return feet
                elif ind == 6 and numFeet == 6:
                    return feet
                elif ind == 7 and numFeet == 2:
                    return feet
                else:
                    return " "
            private assignAfailFreeVerse(code, meter)
                List<string> feet = new List<string>()
                bool f = True
                afail = ""
                residue = meter
                residue = residue.Replace(" ", "")
                residue = residue.Replace("+", " ")
                residue = residue.Replace("/", " ")
                foreach (s in residue.Split(' ')
                    bool flag = True
                    for (int j = 0 j < feet.Count j++)
                        if s == feet[j]:
                            flag = False
                            break
                    if flag:
                    feet.Add(s)
                if len(code) > 0:
                    for (int j = 0 j < len(code) j++)
                        int index = -1
                        for (int k = 0 k < feet.Count k++)
                            bool flag = True
                            index = k
                            if j + feet[k].len > len(code):
                                index = -1
                                flag = False
                            else:
                                slice = code.Substring(j, feet[k].len)
                                for (int z = 0 z < feet[k].len z++)
                                    if not ((slice[z] == feet[k][z]) or (slice[z] == 'x':
                                        flag = False
                                        index = -1
                                        break
                            if flag:
                            break
                        if index >= 0:
                            j = j + feet[index].len - 1
                            afail += Meters.Rukn(feet[index]) + " "
                        else:
                            f = False
                            break
                    if f:
                    pass
                else:
                return afail
                return afail
            private assignMeterFreeVerse(code, meter)
                List<string> feet = new List<string>()
                bool f = True
                afail = ""
                residue = meter
                residue = residue.Replace(" ", "")
                residue = residue.Replace("+", " ")
                residue = residue.Replace("/", " ")
                foreach (s in residue.Split(' ')
                    bool flag = True
                    for (int j = 0 j < feet.Count j++)
                        if s == feet[j]:
                            flag = False
                            break
                    if flag:
                    feet.Add(s)
                if len(code) > 0:
                    for (int j = 0 j < len(code) j++)
                        int index = -1
                        for (int k = 0 k < feet.Count k++)
                            bool flag = True
                            index = k
                            if j + feet[k].len > len(code):
                                index = -1
                                flag = False
                            else:
                                slice = code.Substring(j, feet[k].len)
                                for (int z = 0 z < feet[k].len z++)
                                    if not ((slice[z] == feet[k][z]) or (slice[z] == 'x':
                                        flag = False
                                        index = -1
                                        break
                            if flag:
                            break
                        if index >= 0:
                            j = j + feet[index].len - 1
                            afail += feet[index]
                        else:
                            f = False
                            break
                    if f:
                    pass
                else:
                return afail
                return afail
            public List<scanPath> Scan(int lineNum)
                if lineNum <= numLines:
                    #//// Deal with Noon ghunna case separately later
                    Lines line = lstLines[lineNum]
                    connectionString = TaqtiController.connectionString
                    List<Words> list = new List<Words>()
                    foreach (Words wrd in line.wordsList)
                        code = ""
                        int id = -1
                        stripped = Araab.remove_araab(wrd.word)
                        int length = len(stripped)
                        if wrd.code.Count == 0:
                            Words wd = wordCode(wrd)
                            if wd.id.Count == 0:
                                #////////////// Guesswork /////////////////////////////
                                if wd.id.Count == 0:
                                    originalWord = wrd.word
                                    #wrd.word = Araab.remove_araab(originalWord)
                                    newWord = removeTashdid(wrd.word.Replace("\u06BE", "").Replace("\u06BA", "") #/ remove ھ \u06BE and ں \u06BA for scansion purposes
                                    wrd.length = Araab.remove_araab(wrd.word).len
                                    if wrd.length == 1:
                                        if newWord == "آ":
                                            code = "="
                                        else:
                                            code = "-"
                                    elif wrd.length == 2:
                                        code = length_two_scan(newWord)
                                    elif wrd.length == 3:
                                        code = length_three_scan(newWord)
                                    elif wrd.length == 4:
                                        code = length_four_scan(newWord)
                                    elif wrd.length == 5:
                                        code = length_five_scan(newWord)
                                    if not string.IsNullOrEmpty(code:
                                        if code[len(code) - 1] == "=":   # Word-end flexible syllable
                                            if is_vowel_plus_h(Araab.remove_araab(wrd.word.Replace("ں", "")[Araab.remove_araab(wrd.word.Replace("ں", "").len - 1]:
                                                code = code[:-1]
                                                code += "x"
                                    #GuessWork
                                    if len(stripped) > 4 and code == "":
                                        wd = compoundWord(wd)
                                        if wd.id.Count == 0:
                                            code = "---"
                                            MySqlConnection myConn = new MySqlConnection(connectionString)
                                            myConn.Open()
                                            MySqlCommand cmd = new MySqlCommand(connectionString)
                                            cmd = myConn.CreateCommand()
                                            cmd.CommandText = "select * from unassigned where word like @word"
                                            cmd.Parameters.AddWithValue("@word", Araab.remove_araab(wd.word)
                                            MySqlDataReader dataReader = cmd.ExecuteReader()
                                            if not dataReader.HasRows: # look for existing entry in the unassigned table
                                                myConn.Close()
                                                MySqlConnection myConn2 = new MySqlConnection(connectionString)
                                                myConn2.Open()
                                                MySqlCommand cmd2 = new MySqlCommand(connectionString)
                                                cmd2 = myConn2.CreateCommand()
                                                cmd2.CommandText = "INSERT into unassigned(word,assigned) VALUES (@word,@assigned)"
                                                cmd2.Parameters.AddWithValue("@word", Araab.remove_araab(wd.word)
                                                cmd2.Parameters.AddWithValue("@assigned", False)
                                                cmd2.ExecuteNonQuery()
                                                myConn2.Close()
                                            myConn.Close()
                                        elif code == "":
                                            code = "---"
                                    if wd.id.Count == 0:
                                        wd.word = originalWord
                                        wd.code.Add(code)
                                        wd.id.Add(id)
                            list.Add(wd)
                        else:
                            list.Add(wrd)
                    line.wordsList = list
                    #////////////////////////////  Al (ال) //////////////////////////////////////////////////
                    for (int i = 0 i < line.wordsList.Count - 1 i++)
                        Words wrd = line.wordsList[i]
                        Words nwrd = line.wordsList[i + 1]
                        if nwrd.word.len > 1:
                            if nwrd.word[0] == 'ا' and nwrd.word[1] == 'ل' and (wrd.word[wrd.word.len - 1] == Araab.characters[9] or wrd.word[wrd.word.len - 1] == Araab.characters[8]:
                                stripped = Araab.remove_araab(wrd.word)
                                int length = len(stripped)
                                for (int k = 0 k < wrd.code.Count k++)
                                    if is_vowel_plus_h(stripped[length - 1]:
                                        if wrd.code[k][wrd.code[k].len - 1] == "=") or wrd.code[k][wrd.code[k].len - 1] == "x":
                                            wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                            wrd.code[k] += "="
                                        elif wrd.code[k][wrd.code[k].len - 1] == "-":
                                            wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                            wrd.code[k] += "="
                                    else: #consonant
                                        if Araab.remove_araab(wrd.word).len == 2:
                                            if isConsonantPlusConsonant(wrd.word:
                                                wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                                wrd.code[k] += "=="
                                            else:
                                                wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                                wrd.code[k] += "="
                                        elif wrd.code[k][wrd.code[k].len - 1] == "=") or wrd.code[k][wrd.code[k].len - 1] == "x":
                                            wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                            wrd.code[k] += "-="
                                        elif wrd.code[k][wrd.code[k].len - 1] == "-":
                                            wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                            wrd.code[k] += "="
                                for (int k = 0 k < nwrd.code.Count k++)
                                    nwrd.code[k] = nwrd.code[k][1:]
                                for (int l = 0 l < wrd.muarrab.Count l++)
                                    wrd.muarrab[l] = wrd.muarrab[l] + "ل"
                                for (int l = 0 l < nwrd.muarrab.Count l++)
                                    nwrd.muarrab[l] = nwrd.muarrab[l][2:]
                    #/////////////////////////////  Izafat (اضافت) /////////////////////////////////////////
                    foreach (Words wrd in line.wordsList)
                        if isIzafat(wrd.word:
                            if wrd.id.Count > 0:
                                int count = wrd.code.Count
                                for (int k = 0 k < count k++)
                                    tWord = Araab.remove_araab(wrd.word)
                                    #/////////////////// Arabic Monosyllabic Words $3.2 ///////////////////////////////////////
                                    if wrd.length == 2:
                                        wrd.code[k] = "xx"
                                    #/////////////////// Consonants and other vowels (ی،ے)////////////////////////////////////
                                    elif wrd.code[k][wrd.code[k].len - 1] == "=") or wrd.code[k][wrd.code[k].len - 1] == "x":
                                        if tWord[tWord.len - 1] == 'ا') or tWord[tWord.len - 1] == 'و':
                                            wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                            wrd.code[k] += "=x"
                                        else:
                                            if tWord[tWord.len - 1] == 'ی':
                                                wrd.code.Add(wrd.code[k] + "x")
                                                wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                                wrd.code[k] += "-x"
                                            else:
                                                wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                                wrd.code[k] += "-x"
                                    elif wrd.code[k][wrd.code[k].len - 1] == "-":
                                        wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                        wrd.code[k] += "x"
                            else:
                                for (int k = 0 k < wrd.code.Count k++)
                                    if wrd.code[k][wrd.code[k].len - 1] == "=") or wrd.code[k][wrd.code[k].len - 1] == "x":
                                        wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                        wrd.code[k] += "-x"
                                    elif wrd.code[k][wrd.code[k].len - 1] == "-":
                                        wrd.code[k] = wrd.code[k].Remove(wrd.code[k].len - 1)
                                        wrd.code[k] += "x"
                    #//////////////////////////// Ataf (عطف) ////////////////////////////////////////////
                    for (int i = 1 i < line.wordsList.Count i++)
                        Words wrd = line.wordsList[i]
                        Words pwrd = line.wordsList[i - 1]
                        if wrd.word == "و":
                            stripped = Araab.remove_araab(pwrd.word)
                            int length = len(stripped)
                            for (int k = 0 k < pwrd.code.Count k++)
                                if is_vowel_plus_h(stripped[length - 1]:
                                    if stripped[length - 1] == 'ا' or stripped[length - 1] == 'ی':
                                        # do nothing as it already in correct form
                                    elif stripped[length - 1] == 'ے' or stripped[length - 1] == 'و':
                                        if pwrd.code[k][pwrd.code[k].len - 1] == "=") or pwrd.code[k][pwrd.code[k].len - 1] == "x":
                                            pwrd.code[k] = pwrd.code[k].Remove(pwrd.code[k].len - 1)
                                            pwrd.code[k] += "-x"
                                            for (int j = 0 j < wrd.code.Count j++) wrd.code[j] = ""
                                        elif pwrd.code[k][pwrd.code[k].len - 1] == "-":
                                            pwrd.code[k] = pwrd.code[k].Remove(pwrd.code[k].len - 1)
                                            pwrd.code[k] += "x"
                                            for (int j = 0 j < wrd.code.Count j++) wrd.code[j] = ""
                                    else:
                                        if pwrd.code[k][pwrd.code[k].len - 1] == "=") or pwrd.code[k][pwrd.code[k].len - 1] == "x":
                                            pwrd.code[k] = pwrd.code[k].Remove(pwrd.code[k].len - 1)
                                            pwrd.code[k] += "-x"
                                            for (int j = 0 j < wrd.code.Count j++) wrd.code[j] = ""
                                        elif pwrd.code[k][pwrd.code[k].len - 1] == "-":
                                            pwrd.code[k] = pwrd.code[k].Remove(pwrd.code[k].len - 1)
                                            pwrd.code[k] += "x"
                                            for (int j = 0 j < wrd.code.Count j++) wrd.code[j] = ""
                                else: #consonant
                                    if length == 2 and isConsonantPlusConsonant(Araab.remove_araab(pwrd.word:
                                        pwrd.code[k] = "xx"
                                        for (int j = 0 j < wrd.code.Count j++) wrd.code[j] = ""
                                    elif pwrd.code[k][pwrd.code[k].len - 1] == "=") or pwrd.code[k][pwrd.code[k].len - 1] == "x":
                                        pwrd.code[k] = pwrd.code[k].Remove(pwrd.code[k].len - 1)
                                        pwrd.code[k] += "-x"
                                        for (int j = 0 j < wrd.code.Count j++) wrd.code[j] = ""
                                    elif pwrd.code[k][pwrd.code[k].len - 1] == "-":
                                        pwrd.code[k] = pwrd.code[k].Remove(pwrd.code[k].len - 1)
                                        pwrd.code[k] += "x"
                                        for (int j = 0 j < wrd.code.Count j++) wrd.code[j] = ""
                    #////////////////////////// Word Grafting (وصالِ الف) ////////////////////////////////
                    for (int i = 1 i < line.wordsList.Count i++)
                        Words wrd = line.wordsList[i]
                        Words prevWord = line.wordsList[i - 1]
                        if wrd.word[0] == 'ا' or wrd.word[0] == 'آ':
                            if not is_vowel_plus_h(Araab.remove_araab(prevWord.word)[Araab.remove_araab(prevWord.word).len - 1]:
                                for (int k = 0 k < prevWord.code.Count k++)
                                    if prevWord.code[k][prevWord.code[k].len - 1] == '=':
                                        code = line.wordsList[i - 1].code[k]
                                        code = code.Remove(len(code) - 1)
                                        code = code + "-"
                                        line.wordsList[i - 1].taqtiWordGraft.Add(code)
                                    elif prevWord.code[k][prevWord.code[k].len - 1] == '-':
                                        code = line.wordsList[i - 1].code[k]
                                        code = code.Remove(len(code) - 1)
                                        line.wordsList[i - 1].taqtiWordGraft.Add(code)
                    return findMeter(line)
                return findMeter(new Lines("")
            public int calculateScore(meter, lineFeet)
                List<string> feet = new List<string>()
                residue = ""
                foreach(var m in Meters.meterIndex(meter)
                    residue +=  Meters.Afail(Meters.meters[m]) + " "
                foreach (s in residue.Split(' ')
                    bool flag = True
                    for (int j = 0 j < feet.Count j++)
                        if s.Trim() == feet[j].Trim(:
                            flag = False
                            break
                    if flag and not String.IsNullOrWhiteSpace(s:
                    feet.Add(s.Trim()
                List<string> lineArkan = new List<string>()
                residue = lineFeet
                foreach (s in residue.Split(' ')
                    bool flag = True
                    for (int j = 0 j < lineArkan.Count j++)
                        if s.Trim() == lineArkan[j].Trim(:
                            flag = False
                            break
                    if flag and not String.IsNullOrWhiteSpace(s:
                    lineArkan.Add(s.Trim()
                if lineArkan.Count() == feet.Count(:
                    if isOrdered(lineArkan, feet:
                    return 1
                    else:
                    return 0
                else:
                    return 0
                #return 1.0/Convert.ToDouble(lineArkan.Count()
            public bool isOrdered(List<string> lineArkaan, List<string> feet)
                bool flag = True
                for (int i = 0 i < lineArkaan.Count() i++)
                    if not lineArkaan[i] == feet[i]:
                        flag = False
                        break
                return flag
            public List<scanOutput> crunch(List<scanOutput> list)
                List<scanOutput> lst = new List<scanOutput>()
                List<string> meterNames = new List<string>()
                bool flag = True
                for (int i = 0 i < list.Count() i++)
                    flag = True
                    if meterNames.Count > 0:
                        for (int n = 0 n < meterNames.Count n++)
                            if meterNames[n] == list[i].meterName:
                                flag = False
                                break
                        if flag:
                        meterNames.Add(list[i].meterName)
                    else:
                    meterNames.Add(list[i].meterName)
                double[] scores = new double[meterNames.Count]
                for (int i = 0 i < meterNames.Count i++)
                    for(int j = 0 j<list.Count j++)
                        if list[j].meterName == meterNames[i]:
                            scores[i] += calculateScore(meterNames[i],list[j].feet)
                string[] metes = new string[meterNames.Count()]
                for (int i = 0 i < meterNames.Count i++)
                    metes[i] = meterNames[i]
                Array.Sort(scores, metes)
                finalMeter = metes.Last()
                foreach (var m in list)
                    if m.meterName == finalMeter:
                        lst.Add(m)
                    #for (int i = 0 i < metes.Count() i++)
                    #{
                    #    if m.meterName == metes[i]:
                    #    {
                    #        if scores[i] > 0.0:
                    #        {
                    #            lst.Add(m)
                    #        }
                    #    }
                    #}
                return lst
            public List<scanOutputFuzzy> crunchFuzzy(List<scanOutputFuzzy> list)
                if list.Count > 0:
                    List<scanOutputFuzzy> lst = new List<scanOutputFuzzy>()
                    List<string> meterNames = new List<string>()
                    bool flag = True
                    for (int i = 0 i < list.Count() i++)
                        flag = True
                        if meterNames.Count > 0:
                            for (int n = 0 n < meterNames.Count n++)
                                if meterNames[n] == list[i].meterName:
                                    flag = False
                                    break
                            if flag:
                            meterNames.Add(list[i].meterName)
                        else:
                        meterNames.Add(list[i].meterName)
                    double[] scores = new double[meterNames.Count]
                    double score = 0.0d
                    double count = 0.0d
                    double subtract = 0.0d
                    for (int i = 0 i < meterNames.Count i++)
                        score = 0.0d
                        subtract = 0.0d
                        count = 0.0d
                        for (int j = 0 j < list.Count j++)
                            if list[j].meterName == meterNames[i]:
                                if list[j].score == 0:
                                    score += Math.Log(list[j].score + 1)
                                    count += 1.0d
                                    subtract += 1.0d
                                else:
                                    score += Math.Log(list[j].score)
                                    count += 1.0d
                        scores[i] = Math.Exp(score / count) - subtract
                    string[] metes = new string[meterNames.Count()]
                    for (int i = 0 i < meterNames.Count i++)
                        metes[i] = meterNames[i]
                    Array.Sort(scores, metes)
                    finalMeter = metes.First()
                    foreach (var m in list)
                        #if m.meterName == finalMeter:
                        #{
                        #    lst.Add(m)
                        #}
                        #for (int i = 0 i < metes.Count() i++)
                        #{
                        if m.id == -2:
                            if m.meterName == finalMeter:
                                lst.Add(m)
                        elif Meters.meterIndex(finalMeter).Count > 0:
                            if m.id == Meters.id[Meters.meterIndex(finalMeter).First()]:
                                lst.Add(m)
                    return lst
                else:
                    return list
            public List<scanOutput> scanLines()
                List<scanPath> sp = new List<scanPath>()
                scanOutput so
                List<scanOutput> list = new List<scanOutput>()
                if not fuzzy and not freeVerse:
                    for (int k = 0 k < numLines k++)
                        sp = Scan(k)
                        if sp.Count > 0:
                            int curIndex = list.Count
                            for (int l = 0 l < sp.Count l++)
                                if sp[l].meters.Count > 0:
                                    for (int m = 0 m < sp[l].meters.Count m++)
                                        so = new scanOutput()
                                        so.originalLine = lstLines[k].originalLine
                                        for (int i = 1 i < sp[l].location.Count i++)
                                            so.words.Add(lstLines[k].wordsList[sp[l].location[i].wordRef])
                                            so.wordTaqti.Add(sp[l].location[i].code)
                                            if lstLines[k].wordsList[sp[l].location[i].wordRef].muarrab.Count > sp[l].location[i].codeRef:
                                                so.wordMuarrab.Add(lstLines[k].wordsList[sp[l].location[i].wordRef].muarrab[sp[l].location[i].codeRef])
                                            else:
                                                if lstLines[k].wordsList[sp[l].location[i].wordRef].taqtiWordGraft.Count > 0:
                                                    so.wordMuarrab.Add(lstLines[k].wordsList[sp[l].location[i].wordRef].taqtiWordGraft[0])
                                                else:
                                                    so.wordMuarrab.Add(lstLines[k].wordsList[sp[l].location[i].wordRef].word)
                                        code = ""
                                        for (int x = 0 x < so.wordTaqti.Count x++)
                                            code += so.wordTaqti[x]
                                        int index = sp[l].meters[m]
                                        meter = ""
                                        if index < Meters.numMeters:
                                            so.meterName = Meters.meterNames[index]
                                            if Meters.usage[index] == 0:
                                                List<Feet> feet = Meters.Afail2(Meters.meters[index], code)
                                                foreach (var v in feet)
                                                    so.feet += v.foot + " "
                                                so.feet += " (غیر مستعمل وزن)"
                                            else:
                                                List<Feet> feet = Meters.Afail2(Meters.meters[index], code)
                                                foreach (var v in feet)
                                                    so.feet += v.foot + " "
                                            meter = Meters.meters[index]
                                            so.id = Meters.id[index]
                                        elif index < Meters.numMeters + Meters.numVariedMeters and index >= Meters.numMeters:
                                            so.meterName = Meters.metersVeriedNames[index - Meters.numMeters]
                                            so.feet = Meters.Afail(Meters.metersVaried[index - Meters.numMeters])
                                            meter = Meters.metersVaried[index - Meters.numMeters]
                                        elif index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters and index >= Meters.numMeters + Meters.numVariedMeters:
                                            so.meterName = Meters.rubaiMeterNames[index - Meters.numMeters - Meters.numVariedMeters] + "(رباعی)"
                                            so.feet = Meters.Afail(Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters])
                                            meter = Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters]
                                            so.id = -2
                                        elif index >= Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            so.meterName = Meters.specialMeterNames[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            int ind = index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters
                                            if ind > 7:
                                            so.feet = zamzamaFeet(ind, code)
                                            else:
                                            so.feet = hindiFeet(ind, code)
                                            meter = Meters.specialMeters[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            so.id = -2 - (index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters)
                                        bool flag = False
                                        if index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            mete = "", met1 = "", met2 = "", met3 = "", met4 = ""
                                            met1 = meter.Replace("/", "")
                                            met2 = met1.Replace("+", "") + "-"
                                            met3 = met1.Replace("+", "-") + "-"
                                            met4 = met1.Replace("+", "-")
                                            met1 = met1.Replace("+", "")
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met1
                                            flag = False
                                            met1 = met2
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met2
                                            flag = False
                                            met1 = met3
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met3
                                            flag = False
                                            met1 = met4
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met4
                                            int z = 0
                                            for (int x = 0 x < so.wordTaqti.Count x++)
                                                temp = ""
                                                for (int y = 0 y < so.wordTaqti[x].len y++)
                                                    temp += mete[z]
                                                    z = z + 1
                                                so.wordTaqti[x] = temp
                                            /*
                                            so.feetList = Meters.Afail2(meter, mete)
                                            for (int x = 0 x < so.wordMuarrab.Count x++)
                                                wrd = Scansion.removeTashdid(so.wordMuarrab[x].Replace("\u06BE", "").Replace("\u06BA", "")
                                                cd = so.wordTaqti[x]
                                                so.words[x].breakup.Clear()
                                                z = 0
                                                for (int y = 0 y < cd.len y++)
                                                    if cd[y] == '-':
                                                        syl = ""
                                                        if wrd.len >= z + 1:
                                                            if y == cd.len - 1:  #word-end case
                                                                if not is_muarrab(wrd[z]:
                                                                    syl = wrd[z]
                                                                    so.words[x].breakup.Add(syl)
                                                                    z = z + 1
                                                                    break
                                                                else:
                                                                    z = z + 1
                                                                    y = y - 1
                                                            elif not is_muarrab(wrd[z]:
                                                                if wrd.len > z + 1:
                                                                    if is_muarrab(wrd[z + 1]:
                                                                        syl = wrd[z] + wrd[z + 1]
                                                                        z = z + 2
                                                                    else:
                                                                        syl = wrd[z]
                                                                        z = z + 1
                                                                else:
                                                                    syl = wrd[z]
                                                                    z = z + 1
                                                                so.words[x].breakup.Add(syl)
                                                            else:
                                                                z = z + 1
                                                                y = y - 1
                                                        else:
                                                            syl = wrd[z - 1]
                                                            so.words[x].breakup.Add(syl)
                                                            z = z + 1
                                                    elif cd[y] == '=':
                                                        syl = ""
                                                        if wrd.len >= z + 2:
                                                            if not is_muarrab(wrd[z]:
                                                                if wrd[z] == 'آ' or wrd[z] == 'ؤ':
                                                                    syl = wrd[z]
                                                                    z = z + 1
                                                                elif is_muarrab(wrd[z + 1]:
                                                                    if wrd.len > z + 2:
                                                                        if not is_muarrab(wrd[z + 2]:
                                                                            syl = wrd[z] + wrd[z + 1] + wrd[z + 2]
                                                                            z = z + 3
                                                                        else:
                                                                            z = z + 1
                                                                            y = y - 1
                                                                    else:
                                                                        z = z + 1
                                                                        y = y - 1
                                                                else:
                                                                    if wrd.len > z + 2:
                                                                        if not is_muarrab(wrd[z + 2]:
                                                                            syl = wrd[z] + wrd[z + 1]
                                                                            z = z + 2
                                                                        else:
                                                                            syl = wrd[z] + wrd[z + 1] + wrd[z + 2]
                                                                            z = z + 3
                                                                    else:
                                                                        syl = wrd[z] + wrd[z + 1]
                                                                        z = z + 2
                                                                so.words[x].breakup.Add(syl)
                                                            else:
                                                                z = z + 1
                                                                y = y - 1
                                                        else:
                                                            syl = wrd[z - 1] + "ے"
                                                            so.words[x].breakup.Add(syl)
                                                            z = z + 2
                                                    else:
                                                        break
                                            List<string> sylList = new List<string>()
                                            for (int x = 0 x < so.words.Count x++)
                                                for (int y = 0 y < so.words[x].breakup.Count y++)
                                                    sylList.Add(so.words[x].breakup[y])
                                            z = 0
                                            for (int x = 0 x < so.feetList.Count x++)
                                                wrds = ""
                                                for (int y = 0 y < so.feetList[x].len(code) y++)
                                                    wrds += sylList[z] + "  "
                                                    z = z + 1
                                                so.feetList[x].words = wrds
                                            */
                                        flag = True
                                        if list.Count > 0:
                                            for (int n = curIndex n < list.Count n++)
                                                if list[n].meterName == so.meterName:
                                                    flag = False
                                        if flag:
                                        list.Add(so)
                elif freeVerse:
                    for (int k = 0 k < numLines k++)
                        sp = Scan(k)
                        if sp.Count > 0:
                            int curIndex = list.Count
                            for (int l = 0 l < sp.Count l++)
                                if sp[l].meters.Count > 0:
                                    for (int m = 0 m < sp[l].meters.Count m++)
                                        so = new scanOutput()
                                        so.originalLine = lstLines[k].originalLine
                                        for (int i = 1 i < sp[l].location.Count i++)
                                            so.words.Add(lstLines[k].wordsList[sp[l].location[i].wordRef])
                                            so.wordTaqti.Add(sp[l].location[i].code)
                                        code = ""
                                        for (int x = 0 x < so.wordTaqti.Count x++)
                                            code += so.wordTaqti[x]
                                        int index = sp[l].meters[m]
                                        meter = ""
                                        if index < Meters.numMeters:
                                            so.meterName = Meters.meterNames[index]
                                            so.feet = assignAfailFreeVerse(code, Meters.meters[index])
                                            meter = Meters.meters[index]
                                            so.id = Meters.id[index]
                                        elif index >= Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            so.meterName = Meters.specialMeterNames[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            int ind = index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters
                                            if ind > 7:
                                            so.feet = zamzamaFeet(ind, code)
                                            else:
                                            so.feet = hindiFeet(ind, code)
                                            meter = Meters.specialMeters[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            so.id = -2 - (index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters)
                                        bool flag = False
                                        if index < Meters.numMeters + Meters.numVariedMeters:
                                            mete = ""
                                            mete = assignMeterFreeVerse(code, Meters.meters[index])
                                            if mete.len > 0:
                                                int z = 0
                                                for (int x = 0 x < so.wordTaqti.Count x++)
                                                    temp = ""
                                                    if so.wordTaqti[x].len + z <= mete.len:
                                                        for (int y = 0 y < so.wordTaqti[x].len y++)
                                                            temp += mete[z]
                                                            z = z + 1
                                                        so.wordTaqti[x] = temp
                                                    else:
                                                        int t
                                                        t = 20
                                        flag = True
                                        if list.Count > 0:
                                            for (int n = curIndex n < list.Count n++)
                                                if not string.IsNullOrEmpty(list[n].meterName:
                                                    if list[n].meterName == so.meterName:
                                                        flag = False
                                                else:
                                                    flag = False
                                        if flag:
                                            if not string.IsNullOrEmpty(so.meterName:
                                            list.Add(so)
                    list = crunch(list)
                return list
            public List<scanOutputFuzzy> scanLinesFuzzy()
                List<scanPath> sp = new List<scanPath>()
                scanOutputFuzzy so
                List<scanOutputFuzzy> list = new List<scanOutputFuzzy>()
                for (int k = 0 k < numLines k++)
                    sp = Scan(k)
                    if sp.Count > 0:
                        int curIndex = list.Count
                        for (int l = 0 l < sp.Count l++)
                            if sp[l].meters.Count > 0:
                                for (int m = 0 m < sp[l].meters.Count m++)
                                    so = new scanOutputFuzzy()
                                    so.originalLine = lstLines[k].originalLine
                                    int index = sp[l].meters[m]
                                    meter = ""
                                    if index < Meters.numMeters:
                                        so.meterName = Meters.meterNames[index]
                                        meter = Meters.meters[index]
                                        so.id = Meters.id[index]
                                    elif index < Meters.numMeters + Meters.numVariedMeters and index >= Meters.numMeters:
                                        so.meterName = Meters.metersVeriedNames[index - Meters.numMeters]
                                        meter = Meters.metersVaried[index - Meters.numMeters]
                                    elif index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters and index >= Meters.numMeters + Meters.numVariedMeters:
                                        so.meterName = Meters.rubaiMeterNames[index - Meters.numMeters - Meters.numVariedMeters] + "(رباعی)"
                                        meter = Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters]
                                        so.id = -2
                                    elif index >= Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                        so.meterName = Meters.specialMeterNames[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                        meter = Meters.specialMeters[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                        so.id = -2 - (index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters)
                                    bool flag = False
                                    if index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                        code = ""
                                        for (int x = 0 x < sp[l].location.Count x++)
                                            code += sp[l].location[x].code
                                        originalMeter = meter
                                        meter = meter.Replace("/", "")
                                        meter2 = meter.Replace("+", "") + "~"
                                        meter3 = meter.Replace("+", "~") + "~"
                                        meter4 = meter.Replace("+", "~")
                                        meter = meter.Replace("+", "")
                                        string[] meters = { meter, meter2, meter3, meter4 }
                                        int[] scores = new int[4]
                                        int[] indices = { 0, 1, 2, 3 }
                                        scores[0] = LevenshteinDistance(meter, code)
                                        scores[1] = LevenshteinDistance(meter2, code)
                                        scores[2] = LevenshteinDistance(meter3, code)
                                        scores[3] = LevenshteinDistance(meter4, code)
                                        if scores[1] == 0 or scores[2] == 0 or scores[3] == 0:
                                            Array.Sort(scores, indices)
                                            meter = meters[indices[0]]
                                        else:
                                            meter = meters[0]
                                        string[,] table = matchFuzzy(meter, code)
                                        so.score = Convert.ToInt32(table[0, 2])
                                    flag = True
                                    if list.Count > 0:
                                        for (int n = curIndex n < list.Count n++)
                                            if list[n].id == so.id:
                                                if list[n].score < so.score:
                                                    flag = False
                                                else:
                                                    list[n] = so
                                                    flag = False
                                    if flag:
                                    list.Add(so)
                List<scanOutputFuzzy> listtemp = crunchFuzzy(list)
                if listtemp.Count > 0:
                    List<int> idList = new List<int>()
                    if listtemp.First().id > 0:
                        for (int i = 0 i < Meters.numMeters i++)
                            if listtemp.First().id == Meters.id[i]:
                                idList.Add(i)
                    else:
                        idList.Add(listtemp.First().id)
                    meter = idList
                    list.Clear()
                    errorParam = 7
                    for (int k = 0 k < numLines k++)
                        sp.Clear()
                        for(int ind=0 ind< lstLines[k].wordsList.Count ind++)
                            lstLines[k].wordsList[ind].breakup.Clear()
                            lstLines[k].wordsList[ind].code.Clear()
                            lstLines[k].wordsList[ind].id.Clear()
                            lstLines[k].wordsList[ind].language.Clear()
                            lstLines[k].wordsList[ind].taqti.Clear()
                            lstLines[k].wordsList[ind].taqtiWordGraft.Clear()
                        sp = Scan(k)
                        if sp.Count > 0:
                            int curIndex = list.Count
                            for (int l = 0 l < sp.Count l++)
                                if sp[l].meters.Count > 0:
                                    for (int m = 0 m < sp[l].meters.Count m++)
                                        so = new scanOutputFuzzy()
                                        so.originalLine = lstLines[k].originalLine
                                        int index = sp[l].meters[m]
                                        meter= ""
                                        if index < Meters.numMeters:
                                            so.meterName = Meters.meterNames[index]
                                            if Meters.usage[index] == 0:
                                                so.feet = Meters.Afail(Meters.meters[index]) + " (غیر مستعمل وزن)"
                                            else:
                                                so.feet = Meters.Afail(Meters.meters[index])
                                            meter= Meters.meters[index]
                                            so.id = Meters.id[index]
                                        elif index < Meters.numMeters + Meters.numVariedMeters and index >= Meters.numMeters:
                                            so.meterName = Meters.metersVeriedNames[index - Meters.numMeters]
                                            so.feet = Meters.Afail(Meters.metersVaried[index - Meters.numMeters])
                                            meter= Meters.metersVaried[index - Meters.numMeters]
                                        elif index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters and index >= Meters.numMeters + Meters.numVariedMeters:
                                            so.meterName = Meters.rubaiMeterNames[index - Meters.numMeters - Meters.numVariedMeters] + "(رباعی)"
                                            so.feet = Meters.Afail(Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters])
                                            meter= Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters]
                                            so.id = -2
                                        elif index >= Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            so.meterName = Meters.specialMeterNames[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            so.feet = ""
                                            meter= Meters.specialMeters[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            so.id = -2 - (index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters)
                                        bool flag = False
                                        if index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            code = ""
                                            for (int x = 0 x < sp[l].location.Count x++)
                                                code += sp[l].location[x].code
                                            originalMeter = meterstring
                                            meter= meterstring.Replace("/", "")
                                            meter2 = meterstring.Replace("+", "") + "~"
                                            meter3 = meterstring.Replace("+", "~") + "~"
                                            meter4 = meterstring.Replace("+", "~")
                                            meter= meterstring.Replace("+", "")
                                            string[] meters = { meterstring, meter2, meter3, meter4 }
                                            int[] scores = new int[4]
                                            int[] indices = { 0, 1, 2, 3 }
                                            scores[0] = LevenshteinDistance(meterstring, code)
                                            scores[1] = LevenshteinDistance(meter2, code)
                                            scores[2] = LevenshteinDistance(meter3, code)
                                            scores[3] = LevenshteinDistance(meter4, code)
                                            Array.Sort(scores, indices)
                                            meter= meters[indices[0]]
                                            string[,] table = matchFuzzy(meterstring, code)
                                            so.score = Convert.ToInt32(table[0, 2])
                                            for (int u = table.len / 3 - 1 u >= 0 u--)
                                                if not String.IsNullOrEmpty(table[u, 0]:
                                                    so.meterSyllables.Add(table[u, 0])
                                                    so.codeSyllables.Add(table[u, 1])
                                            int j = 0
                                            for (j = 0 j < table.len / 3 j++)
                                                if String.IsNullOrEmpty(table[j, 1]:
                                                    j--
                                                    break
                                            for (int i = 1 i < sp[l].location.Count i++)
                                                Words wrd = new Words(lstLines[k].wordsList[sp[l].location[i].wordRef])
                                                cd = ""
                                                for (int u = 0 u < sp[l].location[i].len(code) u++)
                                                    if j >= 0:
                                                        if not String.IsNullOrEmpty(table[j, 1]:
                                                            if table[j, 1] == " ":
                                                                cd += "?"
                                                                u--
                                                                wrd.error = True
                                                            elif table[j, 0] == " ":
                                                                if table[j, 1] == "x":
                                                                    cd += "(=)"
                                                                else:
                                                                    cd += "(" + table[j, 1] + ")"
                                                                wrd.error = True
                                                            else:
                                                                if table[j, 1].Contains("]":
                                                                    wrd.error = True
                                                                if table[j, 1] == "x":
                                                                    cd += "="
                                                                else:
                                                                    cd += table[j, 1]
                                                        j--
                                                so.words.Add(wrd)
                                                so.wordTaqti.Add(cd)
                                                so.orignalTaqti.Add(cd.Replace("[", "").Replace("]", "").Replace("?", "").Replace("(", "").Replace(")", "")
                                            if j >= 0:
                                                for (int v = 0 v <= j v++)
                                                    so.wordTaqti[so.wordTaqti.Count - 1] += "?"
                                                    so.words[so.words.Count - 1].error = True
                                        flag = True
                                        if list.Count > 0:
                                            for (int n = curIndex n < list.Count n++)
                                                if list[n].id == so.id:
                                                    if list[n].score < so.score:
                                                        flag = False
                                                    else:
                                                        list[n] = so
                                                        flag = False
                                        if flag:
                                        list.Add(so)
                else:
                    list.Clear()
                return list
            public List<scanOutputFuzzy> scanLineFuzzy(int id)
                List<scanPath> sp = new List<scanPath>()
                scanOutputFuzzy so
                List<scanOutputFuzzy> list = new List<scanOutputFuzzy>()
                for (int k = 0 k < numLines k++)
                    sp = Scan(k)
                    if sp.Count > 0:
                        int curIndex = list.Count
                        for (int l = 0 l < sp.Count l++)
                            if sp[l].meters.Count > 0:
                                for (int m = 0 m < sp[l].meters.Count m++)
                                    so = new scanOutputFuzzy()
                                    so.id = id
                                    so.originalLine = lstLines[k].originalLine
                                    int index = sp[l].meters[m]
                                    meter = ""
                                    if index < Meters.numMeters:
                                        so.meterName = Meters.meterNames[index]
                                        so.feet = Meters.Afail(Meters.meters[index])
                                        meter = Meters.meters[index]
                                        # so.id = Meters.id[index]
                                    elif index < Meters.numMeters + Meters.numVariedMeters and index >= Meters.numMeters:
                                        so.meterName = Meters.metersVeriedNames[index - Meters.numMeters]
                                        so.feet = Meters.Afail(Meters.metersVaried[index - Meters.numMeters])
                                        meter = Meters.metersVaried[index - Meters.numMeters]
                                    elif index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters and index >= Meters.numMeters + Meters.numVariedMeters:
                                        so.meterName = Meters.rubaiMeterNames[index - Meters.numMeters - Meters.numVariedMeters] + "(رباعی)"
                                        so.feet = Meters.Afail(Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters])
                                        meter = Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters]
                                    elif index >= Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                        so.meterName = Meters.specialMeterNames[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                        so.feet = ""
                                        meter = Meters.specialMeters[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                    bool flag = False
                                    if index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                        code = ""
                                        for (int x = 0 x < sp[l].location.Count x++)
                                            code += sp[l].location[x].code
                                        originalMeter = meter
                                        meter = meter.Replace("/", "")
                                        meter2 = meter.Replace("+", "") + "~"
                                        meter3 = meter.Replace("+", "~") + "~"
                                        meter4 = meter.Replace("+", "~")
                                        meter = meter.Replace("+", "")
                                        string[] meters = { meter, meter2, meter3, meter4 }
                                        int[] scores = new int[4]
                                        int[] indices = { 0, 1, 2, 3 }
                                        scores[0] = LevenshteinDistance(meter, code)
                                        scores[1] = LevenshteinDistance(meter2, code)
                                        scores[2] = LevenshteinDistance(meter3, code)
                                        scores[3] = LevenshteinDistance(meter4, code)
                                        Array.Sort(scores, indices)
                                        meter = meters[indices[0]]
                                        string[,] table = matchFuzzy(meter, code)
                                        so.score = Convert.ToInt32(table[0, 2])
                                        for (int u = table.len / 3 - 1 u >= 0 u--)
                                            if not String.IsNullOrEmpty(table[u, 0]:
                                                so.meterSyllables.Add(table[u, 0])
                                                so.codeSyllables.Add(table[u, 1])
                                        int j = 0
                                        for (j = 0 j < table.len / 3 j++)
                                            if String.IsNullOrEmpty(table[j, 1]:
                                                j--
                                                break
                                        for (int i = 1 i < sp[l].location.Count i++)
                                            Words wrd = new Words(lstLines[k].wordsList[sp[l].location[i].wordRef])
                                            cd = ""
                                            for (int u = 0 u < sp[l].location[i].len(code) u++)
                                                if j >= 0:
                                                    if not String.IsNullOrEmpty(table[j, 1]:
                                                        if table[j, 1] == " ":
                                                            cd += "?"
                                                            u--
                                                            wrd.error = True
                                                        elif table[j, 0] == " ":
                                                            if table[j, 1] == "x":
                                                                cd += "(=)"
                                                            else:
                                                                cd += "(" + table[j, 1] + ")"
                                                            wrd.error = True
                                                        else:
                                                            if table[j, 1].Contains("]":
                                                                wrd.error = True
                                                            if table[j, 1] == "x":
                                                                cd += "="
                                                            else:
                                                                cd += table[j, 1]
                                                    j--
                                            so.words.Add(wrd)
                                            so.wordTaqti.Add(cd)
                                            so.orignalTaqti.Add(cd.Replace("[", "").Replace("]", "").Replace("?", "").Replace("(", "").Replace(")", "")
                                        if j > 0:
                                            for (int v = 0 v <= j v++)
                                                so.wordTaqti[so.wordTaqti.Count - 1] += "?"
                                                so.words[so.words.Count - 1].error = True
                                    flag = True
                                    if list.Count > 0:
                                        for (int n = curIndex n < list.Count n++)
                                            if list[n].id == so.id:
                                                if list[n].score < so.score:
                                                    flag = False
                                                else:
                                                    list[n] = so
                                                    flag = False
                                    if flag:
                                    list.Add(so)
                return list
            public List<scanOutput> scanOneLine(int id)
                List<scanPath> sp = new List<scanPath>()
                scanOutput so
                List<scanOutput> list = new List<scanOutput>()
                if not fuzzy and not freeVerse:
                    for (int k = 0 k < numLines k++)
                        sp = Scan(k)
                        if sp.Count > 0:
                            int curIndex = list.Count
                            for (int l = 0 l < sp.Count l++)
                                if sp[l].meters.Count > 0:
                                    for (int m = 0 m < sp[l].meters.Count m++)
                                        so = new scanOutput()
                                        so.originalLine = lstLines[k].originalLine
                                        for (int i = 1 i < sp[l].location.Count i++)
                                            so.words.Add(lstLines[k].wordsList[sp[l].location[i].wordRef])
                                            so.wordTaqti.Add(sp[l].location[i].code)
                                        code = ""
                                        for (int x = 0 x < so.wordTaqti.Count x++)
                                            code += so.wordTaqti[x]
                                        int index = sp[l].meters[m]
                                        meter = ""
                                        if index < Meters.numMeters:
                                            so.meterName = Meters.meterNames[index]
                                            if Meters.usage[index] == 0:
                                                so.feet = Meters.Afail(Meters.meters[index]) + " (غیر مستعمل وزن)"
                                            else:
                                                so.feet = Meters.Afail(Meters.meters[index])
                                            meter = Meters.meters[index]
                                            so.id = Meters.id[index]
                                        elif index < Meters.numMeters + Meters.numVariedMeters and index >= Meters.numMeters:
                                            so.meterName = Meters.metersVeriedNames[index - Meters.numMeters]
                                            so.feet = Meters.Afail(Meters.metersVaried[index - Meters.numMeters])
                                            meter = Meters.metersVaried[index - Meters.numMeters]
                                        elif index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters and index >= Meters.numMeters + Meters.numVariedMeters:
                                            so.meterName = Meters.rubaiMeterNames[index - Meters.numMeters - Meters.numVariedMeters] + "(رباعی)"
                                            so.feet = Meters.Afail(Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters])
                                            meter = Meters.rubaiMeters[index - Meters.numMeters - Meters.numVariedMeters]
                                            so.id = -2
                                        elif index >= Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            so.meterName = Meters.specialMeterNames[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            int ind = index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters
                                            if ind > 7:
                                            so.feet = zamzamaFeet(ind, code)
                                            else:
                                            so.feet = hindiFeet(ind, code)
                                            meter = Meters.specialMeters[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            so.id = -2 - (index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters)
                                        bool flag = False
                                        if index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            mete = "", met1 = "", met2 = "", met3 = "", met4 = ""
                                            met1 = meter.Replace("/", "")
                                            met2 = met1.Replace("+", "") + "-"
                                            met3 = met1.Replace("+", "-") + "-"
                                            met4 = met1.Replace("+", "-")
                                            met1 = met1.Replace("+", "")
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met1
                                            flag = False
                                            met1 = met2
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met2
                                            flag = False
                                            met1 = met3
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met3
                                            flag = False
                                            met1 = met4
                                            if met1.len == len(code):
                                                for (int j = 0 j < met1.len j++)
                                                    char met = met1[j]
                                                    char cd = code[j]
                                                    if met == '-':
                                                        if cd == '-' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                                    elif met == '=':
                                                        if cd == '=' or cd == 'x':
                                                            pass
                                                        else:
                                                            flag = True
                                                            break
                                            else:
                                                flag = True
                                            if not flag:
                                                mete = met4
                                            int z = 0
                                            for (int x = 0 x < so.wordTaqti.Count x++)
                                                temp = ""
                                                for (int y = 0 y < so.wordTaqti[x].len y++)
                                                    temp += mete[z]
                                                    z = z + 1
                                                so.wordTaqti[x] = temp
                                        so.id = id
                                        if numLines > 1:
                                            flag = True
                                            if list.Count > 0:
                                                for (int n = 0 n < list.Count n++)
                                                    if list[n].meterName == so.meterName:
                                                        flag = False
                                            else:
                                                if so.feet.Count() > 0:
                                                list.Add(so)
                                            if not flag:
                                                if so.feet.Count() > 0:
                                                list.Add(so)
                                        else:
                                            flag = True
                                            if list.Count > 0:
                                                for (int n = curIndex n < list.Count n++)
                                                    if list[n].meterName == so.meterName:
                                                        flag = False
                                            if flag:
                                                if so.feet.Count() > 0:
                                                list.Add(so)
                if freeVerse:
                    for (int k = 0 k < numLines k++)
                        sp = Scan(k)
                        if sp.Count > 0:
                            int curIndex = list.Count
                            for (int l = 0 l < sp.Count l++)
                                if sp[l].meters.Count > 0:
                                    for (int m = 0 m < sp[l].meters.Count m++)
                                        so = new scanOutput()
                                        so.originalLine = lstLines[k].originalLine
                                        for (int i = 1 i < sp[l].location.Count i++)
                                            so.words.Add(lstLines[k].wordsList[sp[l].location[i].wordRef])
                                            so.wordTaqti.Add(sp[l].location[i].code)
                                        code = ""
                                        for (int x = 0 x < so.wordTaqti.Count x++)
                                            code += so.wordTaqti[x]
                                        int index = sp[l].meters[m]
                                        meter = ""
                                        if index < Meters.numMeters:
                                            so.meterName = Meters.meterNames[index]
                                            so.feet = assignAfailFreeVerse(code,Meters.meters[index])
                                            meter = Meters.meters[index]
                                            so.id = Meters.id[index]
                                        elif index >= Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            so.meterName = Meters.specialMeterNames[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            int ind = index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters
                                            if ind > 7:
                                            so.feet = zamzamaFeet(ind, code)
                                            else:
                                            so.feet = hindiFeet(ind, code)
                                            meter = Meters.specialMeters[index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters]
                                            so.id = -2 - (index - Meters.numMeters - Meters.numVariedMeters - Meters.numRubaiMeters)
                                        bool flag = False
                                        if index < Meters.numMeters + Meters.numVariedMeters + Meters.numRubaiMeters:
                                            mete = ""
                                            mete= assignMeterFreeVerse(code, Meters.meters[index])
                                            int z = 0
                                            for (int x = 0 x < so.wordTaqti.Count x++)
                                                temp = ""
                                                for (int y = 0 y < so.wordTaqti[x].len y++)
                                                    temp += mete[z]
                                                    z = z + 1
                                                so.wordTaqti[x] = temp
                                        if numLines < 1:
                                            flag = True
                                            if list.Count > 0:
                                                for (int n = 0 n < list.Count n++)
                                                    if list[n].meterName == so.meterName:
                                                        flag = False
                                            else:
                                            list.Add(so)
                                            if not flag:
                                            list.Add(so)
                                        else:
                                            flag = True
                                            if list.Count > 0:
                                                for (int n = curIndex n < list.Count n++)
                                                    if list[n].meterName == so.meterName:
                                                        flag = False
                                            if flag:
                                            list.Add(so)
                return list
