import sqlite3
import os
from scansion import Scansion
from db_setup import migrate_mysql_to_sqlite

def main():
    db_path = "aruuz.db"
    
    # Make sure DB schema exists
    if not os.path.exists(db_path):
        print("Database not found. Initializing schema...")
        mysql_path = r"..\Aruuz.Website\DB\AruuzDB.sql"
        migrate_mysql_to_sqlite(mysql_path, db_path)
    
    # Connect to local SQLite Database
    conn = sqlite3.connect(db_path)
    
    scanner = Scansion(conn)
    
    # Test Sher (from Mirza Ghalib)
    test_line = "نقش فریادی ہے کس کی شوخیِ تحریر کا"
    print(f"Scanning Line: {test_line}")
    
    result = scanner.scan_line(test_line)
    print(f"Result: {result}")
    
    conn.close()

if __name__ == "__main__":
    main()
