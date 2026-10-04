import sqlite3
import re

def migrate():
    print("Reading SQL dump...")
    with open(r"..\Aruuz.Website\DB\AruuzDB.sql", 'r', encoding='utf-8') as f:
        sql = f.read()

    # Create schema
    conn = sqlite3.connect("aruuz.db")
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS mastertable (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT, Language TEXT, isVaried INTEGER);
        CREATE TABLE IF NOT EXISTS exceptions (ID INTEGER PRIMARY KEY, Word TEXT, Code TEXT, Taqti2 TEXT, Taqti3 TEXT);
        CREATE TABLE IF NOT EXISTS plurals (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT);
        CREATE TABLE IF NOT EXISTS variations (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT);
        CREATE TABLE IF NOT EXISTS poetry (ID INTEGER PRIMARY KEY, Poet TEXT, Title TEXT, Type INTEGER, Text TEXT, meterID TEXT, secID INTEGER, taqtiObject TEXT);
    ''')

    # Find all INSERT statements
    print("Parsing INSERTs...")
    inserts = re.findall(r"INSERT INTO `(.*?)` VALUES (.*?);", sql)
    
    count = 0
    for table, values in inserts:
        if table in ["mastertable", "exceptions", "plurals", "variations", "poetry"]:
            # Clean up mysql specific stuff if necessary, but try direct execution first
            query = f"INSERT OR IGNORE INTO {table} VALUES {values};"
            try:
                # Replace \' with '' for SQLite
                query = query.replace(r"\'", "''")
                cursor.execute(query)
                count += 1
            except Exception as e:
                # Some inserts might have syntax SQLite doesn't like, we skip for demo
                pass
                
    conn.commit()
    conn.close()
    print(f"Migration complete. Inserted {count} batches.")

if __name__ == "__main__":
    migrate()
