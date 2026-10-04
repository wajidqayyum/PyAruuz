import sqlite3
import re
import os

def migrate_db():
    print("Reading MySQL dump...")
    with open(r"..\Aruuz.Website\DB\AruuzDB.sql", 'r', encoding='utf-8') as f:
        sql = f.read()

    # Create schema
    conn = sqlite3.connect("aruuz.db")
    cursor = conn.cursor()
    
    # Drop tables to start fresh
    cursor.executescript('''
        DROP TABLE IF EXISTS mastertable;
        DROP TABLE IF EXISTS exceptions;
        DROP TABLE IF EXISTS plurals;
        DROP TABLE IF EXISTS variations;
        DROP TABLE IF EXISTS poetry;
        
        CREATE TABLE mastertable (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT, Language TEXT, isVaried INTEGER, Dummy1 TEXT);
        CREATE TABLE exceptions (ID INTEGER PRIMARY KEY, Word TEXT, Code TEXT, Taqti2 TEXT, Taqti3 TEXT);
        CREATE TABLE plurals (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT, Dummy1 TEXT);
        CREATE TABLE variations (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT, Dummy1 TEXT);
        CREATE TABLE poetry (ID INTEGER PRIMARY KEY, Poet TEXT, Title TEXT, Type INTEGER, Text TEXT, meterID TEXT, secID INTEGER, taqtiObject TEXT);
    ''')

    print("Extracting INSERT statements...")
    
    # Split the SQL dump into statements
    # We can't just split by ';' because ';' can be inside string literals.
    # However, standard mysqldump puts INSERT statements on their own lines or large blocks ending with ';'
    
    # Let's find all INSERT INTO blocks.
    # We use a regex that handles the start of INSERT INTO and captures everything up to the semicolon.
    statements = re.finditer(r"(INSERT INTO `(.*?)` VALUES (.*?));\n", sql, re.DOTALL)
    
    success_count = 0
    fail_count = 0
    
    for match in statements:
        full_statement = match.group(1)
        table_name = match.group(2)
        
        if table_name in ["mastertable", "exceptions", "plurals", "variations", "poetry"]:
            # Convert MySQL syntax to SQLite syntax
            # MySQL escapes single quotes like \', SQLite uses ''
            
            # However, we must be careful not to replace \\'
            query = full_statement + ";"
            
            query = query.replace("\\'", "''")
            query = query.replace("INSERT INTO", "INSERT OR IGNORE INTO")
            
            # Remove \r and \n inside values if they break executescript
            # Actually executescript can handle newlines.
            
            # MySQL \0 for null bytes/false
            query = query.replace("\\0", "0")
            
            try:
                cursor.executescript(query)
                success_count += 1
            except Exception as e:
                print(f"Error inserting into {table_name}: {e}")
                fail_count += 1
                
    conn.commit()
    conn.close()
    
    print(f"Database migration complete. Successfully executed {success_count} INSERT batches.")
    if fail_count > 0:
        print(f"Failed {fail_count} batches.")

if __name__ == "__main__":
    migrate_db()
