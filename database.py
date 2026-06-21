import sqlite3


def create_connection(db_name="library.db"):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
    return conn


def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Эта строка удалит старую таблицу со всеми прошлыми книгами, если она есть
            cursor.execute("DROP TABLE IF EXISTS books")

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    author TEXT NOT NULL,
                    publication_year INTEGER,
                    genre TEXT,
                    number_of_pages INTEGER,
                    number_of_copies INTEGER
                )
            ''')
            conn.commit()
            print("Таблица 'books' успешно пересоздана (очищена от старых данных).")
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")
        finally:
            conn.close()


def insert_books(books_list):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.executemany('''
                INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', books_list)
            conn.commit()
            print(f"Успешно добавлено книг: {len(books_list)}.")
        except sqlite3.Error as e:
            print(f"Ошибка при вставке данных: {e}")
        finally:
            conn.close()


def get_books_by_author(author):
    conn = create_connection()
    books = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
            books = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при поиске книг автора {author}: {e}")
        finally:
            conn.close()
    return books


def delete_book_by_id(book_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
            book = cursor.fetchone()

            if book:
                cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
                conn.commit()
                print(f"Книга с ID {book_id} ('{book[1]}') успешно удалена.")
            else:
                print(f"Книга с ID {book_id} не найдена.")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении книги: {e}")
        finally:
            conn.close()


if __name__ == "__main__":
    create_table()

    initial_books = [
        ("Атака титанов. Том 1", "Хадзимэ Исаяма", 2009, "Темное фэнтези", 208, 12),
        ("Ван-Пис. Том 1", "Эйитиро Ода", 1997, "Приключения", 200, 15),
        ("Наруто. Том 1", "Масаси Кисимото", 1999, "Сёнэн", 192, 18),
        ("Тетрадь смерти. Том 1", "Цугуми Оба", 2003, "Детектив", 200, 10),
        ("Берсерк. Том 1", "Кэнтаро Миура", 1989, "Темное фэнтези", 224, 6),
        ("Магическая битва. Том 1", "Гэгэ Акутами", 2018, "Сёнэн", 192, 14),
        ("Клинок, рассекающий демонов. Том 1", "Коёхару Готогэ", 2016, "Сёнэн", 192, 16),
        ("Человек-бензопила. Том 1", "Тацуки Фудзимото", 2018, "Экшен", 192, 11),
        ("Ванпанчмен. Том 1", "ONE", 2012, "Комедия", 200, 9),
        ("Бакуман. Том 1", "Цугуми Оба", 2008, "Драма", 208, 7)
    ]

    print("\n--- Добавление книг (манги) ---")
    insert_books(initial_books)

    print("\n--- Поиск книг автора 'Цугуми Оба' ---")
    oba_books = get_books_by_author("Цугуми Оба")
    for book in oba_books:
        print(f"ID: {book[0]}, Название: {book[1]}, Год: {book[3]}, Копий: {book[6]}")

    print("\n--- Удаление книги по ID ---")
    delete_book_by_id(1)

    print("\n--- Поиск книг автора 'Хадзимэ Исаяма' после удаления ID 1 ---")
    isayama_books = get_books_by_author("Хадзимэ Исаяма")
    for book in isayama_books:
        print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}")