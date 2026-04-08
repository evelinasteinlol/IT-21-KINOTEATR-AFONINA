import os
import sqlite3

# Настройка путей
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Путь к файлу базы данных
DB_PATH = os.path.join(BASE_DIR, 'database', 'app.db')

# Путь к схеме (schema.sql)
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

def get_connection():
    """Создает подключение с поддержкой имен колонок и связей."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Инициализация базы из schema.sql."""
    if not os.path.exists(SCHEMA_PATH):
        print(f"Ошибка! Файл {SCHEMA_PATH} не найден. Проверь папку проекта.")
        return

    try:
        with get_connection() as conn:
            with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
            print("--- Структура базы данных успешно создана и заполнена ---")
    except sqlite3.Error as e:
        print(f"Ошибка SQLite: {e}")
