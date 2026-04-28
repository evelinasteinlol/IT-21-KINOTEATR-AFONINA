import sys
import os

# Добавляем текущую директорию в путь Python
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from db import init_db
from services import add_movie, add_session, add_cinema_hall
from reports import show_all_movies, show_schedule

def main():
    print("=== Система управления кинотеатром v1.1 ===")
    init_db()

    while True:
        print("\nВыберите роль:")
        print("1. Клиент")
        print("2. Администратор / Владелец")
        print("0. Выйти")
        role_choice = input("Введите номер: ")

        if role_choice == "1":
            # Меню для клиента
            while True:
                print("\n--- Меню клиента ---")
                print("1. Посмотреть список фильмов")
                print("2. Просмотреть расписание сеансов")
                # Пункт 3 ("Забронировать билет") удален
                print("0. Назад")
                choice = input("Выберите действие: ")

                if choice == "1":
                    show_all_movies()
                elif choice == "2":
                    show_schedule()
                elif choice == "0":
                    break
                else:
                    print("Некорректный ввод.")

        elif role_choice == "2":
            # Меню для владельца / администратора
            while True:
                print("\n--- Меню владельца ---")
                print("1. Добавить фильм")
                print("2. Добавить сеанс")
                print("3. Добавить зал")
                print("4. Просмотреть отчёты")
                print("0. Назад")
                choice = input("Выберите действие: ")

                if choice == "1":
                    print("\nДобавление нового фильма")
                    title = input("Название: ")
                    genre = input("Жанр: ")
                    try:
                        duration = int(input("Длительность (мин): "))
                        age_rating = input("Возрастной рейтинг (например, PG-13): ")
                        release_year = int(input("Год релиза: "))
                        description = input("Описание: ")
                        add_movie(title, genre, duration, age_rating, release_year, description)
                        print("Фильм успешно добавлен.")
                    except ValueError:
                        print("Некорректный ввод числовых данных.")
                elif choice == "2":
                    print("\nДобавление нового сеанса")
                    try:
                        movie_id = int(input("ID фильма: "))
                        hall_id = int(input("ID зала: "))
                        start_time = input("Время начала (ГГГГ-ММ-ДД ЧЧ:ММ): ")
                        ticket_price = float(input("Цена билета: "))
                        format_type = input("Формат (2D, 3D, IMAX): ")
                        add_session(movie_id, hall_id, start_time, ticket_price, format_type)
                        print("Сеанс успешно добавлен.")
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                elif choice == "3":
                    print("\nДобавление нового зала")
                    try:
                        name = input("Название зала: ")
                        total_rows = int(input("Количество рядов: "))
                        total_seats = int(input("Количество мест в ряду: "))
                        category = input("Категория зала (например, VIP): ")
                        is_active_input = input("Активен (да/нет): ").lower()
                        is_active = is_active_input in ['да', 'yes', 'y', 'true', '1']
                        add_cinema_hall(name, total_rows, total_seats, category, is_active)
                        print("Зал успешно добавлен.")
                    except ValueError:
                        print("Ошибка при вводе данных.")
                elif choice == "4":
                    # Вызов отчётов (только 2 пункта)
                    print("\nВыберите отчёт:")
                    print("1. Список фильмов")
                    print("2. Расписание сеансов")
                    report_choice = input("Введите номер: ")
                    if report_choice == "1":
                        show_all_movies()
                    elif report_choice == "2":
                        show_schedule()
                    else:
                        print("Некорректный выбор.")
                elif choice == "0":
                    break
                else:
                    print("Некорректный ввод.")

        elif role_choice == "0":
            print("Выход из программы. До свидания!")
            sys.exit()

        else:
            print("Некорректный ввод.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма принудительно остановлена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
