import re

def fix():
    with open("heuristics_auto.py", 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix '):' to ':'
    content = re.sub(r'\):\s*$', ':', content, flags=re.MULTILINE)
    content = re.sub(r'\):\s*:', ':', content)
    content = content.replace("):", ":")
    content = content.replace("::", ":")
    
    # Fix .Remove
    content = re.sub(r'code\.Remove\([^,]+,\s*1\)', 'code[:-1]', content)
    
    # Fix string length
    content = content.replace("code.len", "len(code)")
    content = content.replace("subString", "sub_string")
    content = content.replace("string ", "")
    content = content.replace("true", "True")
    content = content.replace("false", "False")
    content = content.replace("&&", "and")
    content = content.replace("||", "or")
    
    # Fix Araab.characters index errors (unmatched parenthesis)
    content = content.replace("Araab.characters[2])", "Araab.characters[2]")
    content = content.replace("Araab.characters[1])", "Araab.characters[1]")
    content = content.replace("Araab.characters[8])", "Araab.characters[8]")
    content = content.replace("Araab.characters[9])", "Araab.characters[9]")
    content = content.replace("Araab.characters[0])", "Araab.characters[0]")
    
    content = content.replace("))", ")")
    
    # Empty if/elif blocks to pass
    content = re.sub(r'(:\s*\n)(\s*)(elif|else|def)', r'\1\2    pass\n\2\3', content)
    
    with open("heuristics_auto.py", 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix()
