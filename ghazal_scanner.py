import sqlite3
import sys
from scansion import Scansion

def scan_ghazal():
    print("="*60)
    print("      ARUUZ URDU POETRY SCANSION ENGINE - PYTHON PORT")
    print("="*60)
    print("\nPlease paste your Ghazal below.")
    print("When you are finished, type 'END' on a new line and press Enter.\n")
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            if line.strip():
                lines.append(line.strip())
        except EOFError:
            break
            
    if not lines:
        print("No ghazal provided. Exiting.")
        return
        
    print("\n" + "="*60)
    print("                 SCANSION RESULTS")
    print("="*60 + "\n")
    
    try:
        conn = sqlite3.connect("aruuz.db")
        from scansion_detailed import ScansionDetailed
        scanner = ScansionDetailed(conn)
        
        results = scanner.scan_poem_detailed("\n".join(lines))
        
        if results and results.get("dominant_meter"):
            print(f"\nDominant Meter: {results['dominant_meter']}")
            print("="*60 + "\n")
            
            for line_data in results["lines"]:
                print(line_data["meter_name"])
                if line_data["feet_names"]:
                    print("\t".join(line_data["feet_names"]))
                
                print("\t".join(line_data["words"]))
                print("\t".join(line_data["codes"]))
                
                print(f"Distance: {line_data['distance']}\n")
        else:
            print("Could not determine scansion.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            
if __name__ == "__main__":
    scan_ghazal()
