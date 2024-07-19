from utils.file_manager import FileManager

FILE = '../data/data.json'


class Book:
    '''
    Класс книги
    '''
    def __init__(self, title: str, author: str, year: int, book_id: int | None = None, status=True):
        self.book_id = book_id if book_id else FileManager.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f'{self.author} - {self.title} ({self.year}), {'доступна' if self.status else 'выдана'}'


class BookManager:
    '''
    Класс работы с книгами
    '''
    @staticmethod
    def __from_book_to_dict(book: Book) -> dict:
        '''
        преобразует экземпляр класса Book в словарь
        '''
        return {
            'id': book.book_id,
            'data': {
                'author': book.author,
                'title': book.title,
                'year': book.year,
                'status': book.status,
            }
        }

    @staticmethod
    def __from_dict_to_book(d: dict) -> Book:
        '''
        преобразует словарь в экземпляр класса Book
        '''
        return Book(
            book_id=d.get('id'),
            author=d.get('data').get('author'),
            title=d.get('data').get('title'),
            year=d.get('data').get('year'),
            status=d.get('data').get('status'),
        )

    @staticmethod
    def __get_all(file=FILE) -> list[Book]:
        data = FileManager.read_json(file)
        result = []
        for d in data:
            result.append(BookManager.__from_dict_to_book(d))
        return result

    @staticmethod
    def get_books(keyword='', file=FILE):
        '''
        метод для вывода книг по ключевому слову
        '''
        data = FileManager.read_json(file)
        result = []

        # без дополнительных условий вернем весь список
        if not keyword:
            for d in data:
                result.append(BookManager.__from_dict_to_book(d))
            return result

        # если принимает 4-значное число, то ищем дополнительно по году выпуска
        # 1984 Оруэлла найдется по запросу '1949'
        if keyword.isdigit() and len(keyword) == 4:
            digit_keyword = int(keyword)
            for d in data:
                if d.get('data').get('year') == digit_keyword:
                    result.append(BookManager.__from_dict_to_book(d))

        # этот цикл ищет по названию и автору
        # 1984 Оруэлла найдется по запросу '1984'
        for d in data:
            if keyword.lower() in d.get('data').get('author').lower() \
                    or keyword.lower() in d.get('data').get('title').lower():
                result.append(BookManager.__from_dict_to_book(d))
        if not result:
            print('Ничего не найдено')
        return result

    @staticmethod
    def add_book(book: Book, file=FILE) -> None:
        '''
        добавляет книгу
        '''
        new_book = BookManager.__from_book_to_dict(book)
        FileManager.write_new_data(new_book, file)

    @staticmethod
    def delete_book(book_id: int, file=FILE) -> None:
        '''
        удаляет книгу
        '''
        data = FileManager.read_json(file)
        for d in data:
            if d.get('id') == book_id:
                data.remove(d)
                print('Книга успешно удалена')
                FileManager.write_data(data, file)
                return
        print('Книги с таким id не найдено')

    @staticmethod
    def update_status(book_id: int, status: bool, file=FILE) -> None:
        '''
        меняет статус книги
        '''
        data = FileManager.read_json(file)
        for d in data:
            if d.get('id') == book_id:
                d['data']['status'] = status
                print('Статус изменен')
                FileManager.write_data(data)
                return
        print('Книги с таким id не найдено')
