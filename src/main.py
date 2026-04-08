import sys
from db import init_db
from services import add_movie, add_session, add_department, add_employee
from reports import show_all_movies  # Импортируем функцию отчета

def main():
    print("=== Система управления кинотеатром v1.0 ===")
    # Инициализация базы данных (если требуется)
    init_db()

    while True:
        print("\nВыберите действие:")
        print("1. Показать все фильмы (Отчет)")
        print("2. Добавить новый фильм")
        print("3. Добавить сеанс")
        print("4. Добавить отдел")
        print("5. Добавить сотрудника")
        print("0. Выход")

        choice = input("\nВведите номер: ")

        if choice == "1":
            # вызываем функцию отображения фильмов
            show_all_movies()

        elif choice == "2":
            print("\nДобавление нового фильма")
            title = input("Название: ")
            genre = input("Жанр: ")
            duration = int(input("Длительность (мин): "))
            age_rating = input("Возрастной рейтинг: ")
            release_year = int(input("Год релиза: "))
            description = input("Описание: ")
            add_movie(title, genre, duration, age_rating, release_year, description)
            print("Фильм успешно добавлен.")

        elif choice == "3":
            print("\nДобавление нового сеанса")
            try:
                movie_id = int(input("ID фильма: "))
                hall_id = int(input("ID зала: "))
                start_time = input("Время начала (ГГГГ-ММ-ДД ЧЧ:ММ): ")
                ticket_price = float(input("Цена билета: "))
                format_type = input("Формат (2D, 3D, IMAX): ")
                add_session(movie_id, hall_id, start_time, ticket_price, format_type)
                print("Сеанс успешно добавлен.")
            except ValueError:
                print("Ошибка: проверьте ввод данных.")

        elif choice == "4":
            print("\nДобавление нового отдела")
            name = input("Название отдела: ")
            add_department(name)
            print("Отдел успешно добавлен.")

        elif choice == "5":
            print("\nДобавление нового сотрудника")
            full_name = input("ФИО: ")
            try:
                dept_id = int(input("ID отдела: "))
                add_employee(full_name, dept_id)
                print("Сотрудник успешно добавлен.")
            except ValueError:
                print("Ошибка: ID отдела должно быть числом.")

        elif choice == "0":
            print("Завершение работы. До свидания!")
            sys.exit()

        else:
            print("Ошибка: введите число из списка.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма принудительно остановлена.")

