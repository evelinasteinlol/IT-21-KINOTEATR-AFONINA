  m.movie_id,
        m.title,
        m.genre,
        m.duration,
        m.age_rating,
        m.release_year,
        m.description,
        d.name AS director_name
    FROM movies m
    LEFT JOIN directors d ON m.director_id = d.director_id
    ORDER BY m.movie_id;
    """

    try:
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            if not rows:
                print("\n[!] Список фильмов пуст.")
                return

            print("\n" + "=" * 120)
            print(
                f"{'ID':<3} | {'Название':<20} | {'Жанр':<10} | {'Длительность':<12} | {'Рейтинг':<8} | {'Год':<4} | {'Описание':<25} | {'Режиссер'}")
            print("-" * 120)

            for row in rows:
                print(
                    f"{row['movie_id']:<3} | {row['title']:<20} | {row['genre']:<10} | {row['duration']:^12} | {row['age_rating']:<8} | {row['release_year']:<4} | {row['description'][:25]:<25} | {row['director_name']}")

            print("=" * 120)

    except Exception as e:
        print(f"Ошибка при формировании отчета: {e}")
