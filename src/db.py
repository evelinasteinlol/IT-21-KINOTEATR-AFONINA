import sqlite3
import os

DB_PATH = "cinema.db"

def init_db():
    """Инициализация базы данных и создание таблиц"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Создание таблиц согласно схеме
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cinema_Halls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            total_rows INTEGER,
            total_seats INTEGER,
            category TEXT,
            is_active BOOLEAN
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            genre TEXT,
            duration INTEGER,
            age_rating TEXT,
            release_year INTEGER,
            description TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            hall_id INTEGER,
            start_time DATETIME,
            price DECIMAL(10,2),
            format TEXT,
            FOREIGN KEY (hall_id) REFERENCES Cinema_Halls(id),
            FOREIGN KEY (movie_id) REFERENCES Movies(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            row_number INTEGER,
            seat_number INTEGER,
            sale_time DATETIME,
            status TEXT,
            FOREIGN KEY (session_id) REFERENCES Sessions(id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("База данных успешно инициализирована")

def get_db_connection():
    """Получение соединения с базой данных"""
    return sqlite3.connect(DB_PATH)
