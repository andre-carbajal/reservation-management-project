import sqlite3

from login import LoginWindow


# Andre Carbajal
def create_user_database():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS reservaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL,
        tipo TEXT NOT NULL,
        precio REAL NOT NULL,
        fecha TEXT NOT NULL,
        hora TEXT NOT NULL,
        terminado BOOLEAN NOT NULL
    )
    ''')
    cursor.execute('''
    INSERT OR IGNORE INTO usuarios (email, password) VALUES (?, ?)
    ''', ('admin@example.com', 'adminpassword'))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_user_database()
    LoginWindow()
