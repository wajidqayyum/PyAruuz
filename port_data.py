import re
import os

def port_meters(cs_path, py_path):
    print("Porting Meters.cs to Python...")
    with open(cs_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract arrays
    def extract_array(var_type, var_name, is_string=False):
        # Matches: static public string[] meterNames = { ... };
        pattern = rf"static\s+public\s+{var_type}\[\]\s+{var_name}\s*=\s*{{(.*?)\}};"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            data = match.group(1).strip()
            # Clean up newlines and comments
            data = re.sub(r'//.*', '', data)
            data = re.sub(r'\s+', ' ', data)
            return data
        return None

    meter_names = extract_array("string", "meterNames")
    meters = extract_array("string", "meters")
    
    with open(py_path, 'w', encoding='utf-8') as f:
        f.write("# Automatically ported from Meters.cs\n\n")
        f.write("class Meters:\n")
        f.write("    meter_names = [\n")
        # meter_names is a comma separated list of strings
        names_list = re.findall(r'"(.*?)"', meter_names)
        for n in names_list:
            f.write(f'        "{n}",\n')
        f.write("    ]\n\n")
        
        f.write("    meters = [\n")
        meters_list = re.findall(r'"(.*?)"', meters)
        for m in meters_list:
            f.write(f'        "{m}",\n')
        f.write("    ]\n")

    print(f"Successfully ported {len(names_list)} meters to {py_path}!")

if __name__ == "__main__":
    cs_file = r"..\Aruuz.Website\Models\Meters.cs"
    py_file = "meters.py"
    port_meters(cs_file, py_file)
