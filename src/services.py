from db import get_db_connection
from datetime import datetime

def add_movie(title, genre, duration, age_rating, release_year, description):
    """Добавление нового фильма"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO Movies (title, genre, duration, age_rating, release_year, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, genre, duration, age_rating, release_year, description))
    
    conn.commit()
    conn.close()

def add_session(movie_id, hall_id, start_time, price, format_type):
    """Добавление нового сеанса"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Проверка существования фильма и зала
    cursor.execute("SELECT id FROM Movies WHERE id = ?", (movie_id,))
    if not cursor.fetchone():
        conn.close()
        raise ValueError(f"Фильм с ID {movie_id} не найден")
    
    cursor.execute("SELECT id FROM Cinema_Halls WHERE id = ?", (hall_id,))
    if not cursor.fetchone():
        conn.close()
        raise ValueError(f"Зал с ID {hall_id} не найден")
    
    cursor.execute('''
        INSERT INTO Sessions (movie_id, hall_id, start_time, price, format)
        VALUES (?, ?, ?, ?, ?)
    ''', (movie_id, hall_id, start_time, price, format_type))
    
    conn.commit()
    conn.close()

def add_cinema_hall(name, total_rows, total_seats, category, is_active):
    """Добавление нового зала"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO Cinema_Halls (name, total_rows, total_seats, category, is_active)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, total_rows, total_seats, category, is_active))
    
    conn.commit()
    conn.close()
