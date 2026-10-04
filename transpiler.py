import re

def transpile_csharp_to_python():
    cs_file = r"..\Aruuz.Website\Models\Scansion.cs"
    py_file = "heuristics_auto.py"
    
    with open(cs_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out_lines = []
    out_lines.append("from araab import Araab\n")
    out_lines.append("from heuristics import *\n\n")
    
    in_method = False
    indent_level = 0
    
    for line in lines:
        original = line
        line = line.strip()
        
        # Start of a length scan method
        match = re.match(r"public\s+string\s+(length[a-zA-Z]+Scan)\(string\s+([a-zA-Z0-9_]+)\)", line)
        if match:
            in_method = True
            method_name = match.group(1)
            # convert camelCase to snake_case
            snake_name = re.sub(r'(?<!^)(?=[A-Z])', '_', method_name).lower()
            arg_name = match.group(2)
            out_lines.append(f"def {snake_name}({arg_name}):\n")
            indent_level = 1
            continue
            
        if not in_method:
            # We only care about the length scan methods
            if "public string NoonGhunna" in line:
                in_method = True
                out_lines.append("def noon_ghunna(word, code):\n")
                indent_level = 1
            continue
            
        if "return code;" in line and indent_level == 1:
            out_lines.append("    return code\n\n")
            in_method = False
            continue
            
        # Skip brackets but handle indentation
        if line == "{":
            indent_level += 1
            continue
        if line == "}":
            indent_level -= 1
            continue
            
        if line.startswith("#region") or line.startswith("#endregion"):
            continue
            
        # Basic replacements
        line = line.replace("string code = \"\";", "code = \"\"")
        line = line.replace("string subString =", "sub_string =")
        line = line.replace("string stripped =", "stripped =")
        line = line.replace("string loc =", "loc =")
        
        line = re.sub(r'//(.*)', r'#\1', line)
        line = line.replace("||", "or")
        line = line.replace("&&", "and")
        line = line.replace("!", "not ")
        
        line = re.sub(r'else if\s*\((.*)\)', r'elif \1:', line)
        line = re.sub(r'if\s*\((.*)\)', r'if \1:', line)
        line = line.replace("else", "else:")
        
        # Method calls
        line = line.replace("Araab.removeAraab", "Araab.remove_araab")
        line = line.replace(".Equals", " == ")
        line = line.replace(".ToString()", "")
        line = line.replace("Length", "len")
        line = line.replace("isVowelPlusH", "is_vowel_plus_h")
        line = line.replace("isMuarrab", "is_muarrab")
        line = line.replace("locateAraab", "locate_araab")
        line = line.replace("containsNoon", "contains_noon")
        
        # Substring / string removal
        line = re.sub(r'\.Remove\(\s*0\s*,\s*(\d+)\s*\)', r'[\1:]', line)
        line = line.replace(";", "")
        
        # Hack for len(stripped) because 'stripped.Length' becomes 'stripped.len'
        line = line.replace("stripped.len", "len(stripped)")
        line = line.replace("substr.len", "len(substr)")
        
        # Convert nested length calls
        line = re.sub(r'length([a-zA-Z]+)Scan', lambda m: 'length_' + m.group(1).lower() + '_scan', line)
        
        if line:
            # Fix parenthesis for ==
            line = line.replace(" == (", " == ")
            line = line.replace(") :", ":")
            # If the line ends with ':' but has extra closing parens from the regex
            if line.endswith("):"):
                pass # usually fine
            
            out_lines.append("    " * indent_level + line + "\n")

    with open(py_file, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
        
    print(f"Transpilation complete! Saved to {py_file}")

if __name__ == "__main__":
    transpile_csharp_to_python()
