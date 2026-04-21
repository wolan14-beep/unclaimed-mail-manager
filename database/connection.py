import sqlite3
from config import DATABASE_PATH

def create_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection


def create_tables(connected):
    cursor = connected.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users( 
                    registration INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    profile TEXT NOT NULL
                      )
                    """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS parcels(
                    order_number INTEGER PRIMARY KEY AUTOINCREMENT,
                    tracking TEXT UNIQUE,
                    sender TEXT,
                    entry_date DATE NOT NULL,
                    exit_date DATE NOT NULL,
                    status TEXT DEFAULT 'Aguardando Refugo',
                    changed_by TEXT,
                    change_date TEXT
                      )
                    """)
    

    connected.commit()