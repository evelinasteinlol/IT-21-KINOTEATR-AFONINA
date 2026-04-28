 from db import get_db_connection

def show_all_movies():
    """Показать все фильмы"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, title, genre, duration, age_rating, release_year 
        FROM Movies 
        ORDER BY title
    ''')
    
    movies = cursor.fetchall()
    
    if not movies:
        print("Фильмы не найдены")
    else:
        print("\n=== Список фильмов ===")
        print(f"{'ID':<3} {'Название':<30} {'Жанр':<15} {'Длительность':<12} {'Возраст':<8} {'Год':<5}")
        print("-" * 80)
        for movie in movies:
            id, title, genre, duration, age_rating, year = movie
            print(f"{id:<3} {title:<30} {genre:<15} {duration} мин      {age_rating:<8} {year:<5}")
    
    conn.close()

def show_schedule():
    """Показать расписание сеансов"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT s.id, m.title, h.name, s.start_time, s.price, s.format
        FROM Sessions s
        JOIN Movies m ON s.movie_id = m.id
        JOIN Cinema_Halls h ON s.hall_id = h.id
        ORDER BY s.start_time
    ''')
    
    sessions = cursor.fetchall()
    
    if not sessions:
        print("Сеансы не найдены")
    else:
        print("\n=== Расписание сеансов ===")
        print(f"{'ID':<3} {'Фильм':<25} {'Зал':<15} {'Время':<20} {'Цена':<8} {'Формат':<8}")
        print("-" * 85)
        for session in sessions:
            id, title, hall, start_time, price, format_type = session
            print(f"{id:<3} {title:<25} {hall:<15} {start_time:<20} {price:<8} {format_type:<8}")
    
    conn.close()

def show_revenue():
    """Показать отчет о доходах"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Доход по сеансам (потенциальный, если бы все места были проданы)
    cursor.execute('''
        SELECT 
            s.id,
            m.title,
            h.name,
            s.start_time,
            s.price,
            h.total_rows * h.total_seats as total_seats,
            s.price * (h.total_rows * h.total_seats) as potential_revenue
        FROM Sessions s
        JOIN Movies m ON s.movie_id = m.id
        JOIN Cinema_Halls h ON s.hall_id = h.id
        ORDER BY s.start_time
    ''')
    
    sessions = cursor.fetchall()
    
    if not sessions:
        print("Сеансы не найдены")
    else:
        print("\n=== Отчет о доходах (потенциальный) ===")
        print(f"{'ID':<3} {'Фильм':<20} {'Зал':<12} {'Время':<16} {'Цена':<8} {'Мест':<5} {'Потенциал':<10}")
        print("-" * 80)
        
        total_potential = 0
        for session in sessions:
            id, title, hall, start_time, price, total_seats, potential = session
            print(f"{id:<3} {title:<20} {hall:<12} {start_time:<16} {price:<8} {total_seats:<5} {potential:<10}")
            total_potential += potential
        
        print("-" * 80)
        print(f"Общий потенциальный доход: {total_potential:.2f}")
    
    conn.close()
