from utils.book import Book, BookManager
from utils.file_manager import FileManager


def main():
    '''
    только меню и ничего лишнего
    '''
    FILE = 'data/data.json'

    while True:
        ans = input('1 - Показать все книги\n2 - Добавить книгу\n3 - Изменить статус\n'
                    '4 - Удалить книгу\n5 - Поиск книг\n6 - Выход\n')
        match ans:
            case '1':
                books = BookManager.get_books(file=FILE)
                for b in books:
                    print(b)
                print()
            case '2':
                print('Добавляем книгу\n')
                author = input('Введите автора: ')
                title = input('Введите название: ')
                year = input('Введите год: ')
                try:
                    book = Book(
                        author=author,
                        title=title,
                        year=int(year)
                    )
                    BookManager.add_book(book, file=FILE)
                except ValueError:
                    print('Введены некорректные данные\n')
                finally:
                    print('\n')
            case '3':
                book_id = input('Введите id книги: ')
                status = input('Введите статус (1 - доступна, 0 - выдана): ')
                if book_id.isdigit() and status.strip() in ['0', '1']:
                    book_id = int(book_id)
                    status = bool(int(status))
                    BookManager.update_status(book_id, status, file=FILE)
                else:
                    print('Введены некорректные данные\n')
                print('\n')
            case '4':
                book_id = input('Введите id книги: ')
                if book_id.isdigit():
                    BookManager.delete_book(int(book_id), file=FILE)
                else:
                    print('Введены некорректные данные\n')
            case '5':
                keyword = input('Введите запрос: ')
                print('\n')
                books = BookManager.get_books(keyword, file=FILE)
                for b in books:
                    print(b)
                print('\n')
            case '6':
                break
            case _:
                continue


if __name__ == '__main__':
    main()
