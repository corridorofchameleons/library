class Book:
    '''
    Класс книги
    '''
    def __init__(self, title: str, author: str, year: int):
        self.id = 1
        self.title = title
        self.author = author
        self.year = year
        self.status = True

    def __str__(self):
        return f'{self.author} - {self.title} ({self.year})'


class BookManager:
    @staticmethod
    def get_all() -> list[Book]:
        pass

    @staticmethod
    def get_book_by_title(title: str) -> list[Book]:
        pass

    @staticmethod
    def get_book_by_author(author: str) -> list[Book]:
        pass

    @staticmethod
    def get_book_by_year(year: int) -> list[Book]:
        pass

    @staticmethod
    def add_book(book: Book) -> None:
        pass

    @staticmethod
    def delete_book(book_id: int) -> None:
        pass

    @staticmethod
    def change_status(book: Book) -> None:
        pass
