import sqlite3
from db import get_connection

def add_employee(full_name, dept_id):
    """
    Добавляет нового сотрудника в таблицу employees.
    :param full_name: Строка с именем сотрудника
    :param dept_id: ID отдела (число)
    """
    query = "INSERT INTO employees (full_name, dept_id) VALUES (?, ?)"
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (full_name, dept_id))
            conn.commit()  # Сохраняем изменения
            print(f"Успех: Сотрудник '{full_name}' добавлен в базу.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: Не удалось добавить сотрудника. Проверьте ID отдела. ({e})")
    except sqlite3.Error as e:
        print(f"Произошла ошибка при работе с БД: {e}")

def add_department(name):
    """Добавляет новый отдел (справочник)"""
    query = "INSERT INTO departments (name) VALUES (?)"
    try:
        with get_connection() as conn:
            conn.execute(query, (name,))
            conn.commit()
            print(f"Отдел '{name}' успешно создан.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании отдела: {e}")

def add_movie(title, genre, duration, age_rating, release_year, description):
    """
    Добавляет новый фильм в таблицу movies.
    :param title: Название фильма
    :param genre: Жанр
    :param duration: Длительность (мин)
    :param age_rating: Рейтинг (например, "16+")
    :param release_year: Год релиза
    :param description: Описание
    """
    query = """
    INSERT INTO movies (title, genre, duration, age_rating, release_year, description)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        with get_connection() as conn:
            conn.execute(query, (title, genre, duration, age_rating, release_year, description))
            conn.commit()
            print(f"Фильм '{title}' успешно добавлен.")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении фильма: {e}")

def add_session(movie_id, hall_id, start_time, ticket_price, format_type):
    """
    Добавляет новый сеанс.
    :param movie_id: ID фильма
    :param hall_id: ID зала
    :param start_time: Время начала (строка)
    :param ticket_price: Цена билета (float)
    :param format_type: Формат (2D, 3D, IMAX)
    """
    query = """
    INSERT INTO sessions (movie_id, hall_id, start_time, ticket_price, format_type)
    VALUES (?, ?, ?, ?, ?)
    """
    try:
        with get_connection() as conn:
            conn.execute(query, (movie_id, hall_id, start_time, ticket_price, format_type))
            conn.commit()
            print("Сеанс успешно добавлен.")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении сеанса: {e}")

# Здесь вы можете добавлять дополнительные функции для работы с другими таблицами
