# modules/database.py
import sqlite3
import numpy as np

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect('database/users.db')

def create_table():
    """Create the users table if it doesn't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            face_encoding BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(name, face_encoding):
    """Insert a new user into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, face_encoding) VALUES (?, ?)", 
                   (name, face_encoding.tobytes()))
    conn.commit()
    conn.close()

def get_all_users():
    """Fetch all users from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, face_encoding FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

if __name__ == "__main__":
    create_table()
    print("Database table created successfully!")