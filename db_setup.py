import sqlite3
import os

def migrate_mysql_to_sqlite(mysql_file, sqlite_file):
    """
    Creates the necessary tables for SQLite. 
    Note: For a full 9MB SQL dump migration, we recommend using a tool like DBeaver or a dedicated MySQL to SQLite Python script.
    """
    print("Connecting to SQLite...")
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    
    # Basic schema conversion for essential tables
    tables = {
        "mastertable": "CREATE TABLE IF NOT EXISTS mastertable (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT, Language TEXT, isVaried INTEGER)",
        "exceptions": "CREATE TABLE IF NOT EXISTS exceptions (ID INTEGER PRIMARY KEY, Word TEXT, Code TEXT, Taqti2 TEXT, Taqti3 TEXT)",
        "plurals": "CREATE TABLE IF NOT EXISTS plurals (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT)",
        "variations": "CREATE TABLE IF NOT EXISTS variations (ID INTEGER PRIMARY KEY, Word TEXT, Muarrab TEXT, Taqti TEXT)",
        "poetry": "CREATE TABLE IF NOT EXISTS poetry (ID INTEGER PRIMARY KEY, Poet TEXT, Title TEXT, Type INTEGER, Text TEXT, meterID TEXT, secID INTEGER, taqtiObject TEXT)"
    }
    
    for table, create_stmt in tables.items():
        cursor.execute(create_stmt)
        print(f"Created table {table}")
        
    conn.commit()
    conn.close()
    print(f"SQLite DB schema created at {sqlite_file}.")
    print("IMPORTANT: Since AruuzDB.sql is an 8.9MB MySQL file, you should convert it to SQLite using a tool like 'sqlite3' command line or a GUI tool like DBeaver to preserve all data accurately.")

if __name__ == "__main__":
    mysql_path = r"..\Aruuz.Website\DB\AruuzDB.sql"
    sqlite_path = "aruuz.db"
    
    migrate_mysql_to_sqlite(mysql_path, sqlite_path)
