import pytest

from utils.book import Book, BookManager
from utils.file_manager import FileManager

TEST_FILE = 'test_data/test_data.json'


@pytest.fixture()
def book():
    return Book('Title', 'Author', 1990, book_id=1)


def test_init(book):
    assert book.book_id == 1
    assert book.title == 'Title'
    assert book.author == 'Author'
    assert book.year == 1990
    assert book.status == True


def test_str(book):
    assert book.__str__() == 'Author - Title (1990), доступна'


def test_from_book_to_dict(book):
    d = BookManager._BookManager__from_book_to_dict(book)
    assert d == {
        'id': 1,
        'data': {
            'author': 'Author',
            'title': 'Title',
            'year': 1990,
            'status': True,
        }
    }


def test_from_dict_to_book():
    d = {
        'id': 1,
        'data': {
            'author': 'Author',
            'title': 'Title',
            'year': 1990,
            'status': True,
        }
    }
    test_book = BookManager._BookManager__from_dict_to_book(d)
    assert test_book.book_id == 1
    assert test_book.title == 'Title'
    assert test_book.author == 'Author'
    assert test_book.year == 1990
    assert test_book.status == True


def test_get_all():
    FileManager.clear(TEST_FILE)
    FileManager.write_data({
        'id': 1,
        'data': {
            'author': 'Author',
            'title': 'Title',
            'year': 1990,
            'status': True,
        }
    }, TEST_FILE)

    data = BookManager.get_all(TEST_FILE)
    assert len(data) == 1

    FileManager.clear(TEST_FILE)


def test_add_book(book):
    FileManager.clear(TEST_FILE)

    BookManager.add_book(book, TEST_FILE)
    data = BookManager.get_all(TEST_FILE)
    assert len(data) == 1

    BookManager.add_book(book, TEST_FILE)
    data = BookManager.get_all(TEST_FILE)
    assert len(data) == 2

    FileManager.clear(TEST_FILE)


def test_delete_book(book):
    FileManager.clear(TEST_FILE)

    BookManager.add_book(book, TEST_FILE)

    BookManager.delete_book(2, TEST_FILE)
    data = BookManager.get_all(TEST_FILE)
    assert len(data) == 1

    BookManager.delete_book(1, TEST_FILE)
    data = BookManager.get_all(TEST_FILE)
    assert len(data) == 0

    FileManager.clear(TEST_FILE)


def test_update_status(book):
    FileManager.clear(TEST_FILE)

    BookManager.add_book(book, TEST_FILE)

    BookManager.update_status(1, False, TEST_FILE)

    books = BookManager.get_all()
    assert books[0].status == False

    FileManager.clear(TEST_FILE)


def test_get_books():
    FileManager.clear(TEST_FILE)

    BookManager.add_book(Book(
        book_id=1,
        author='George Orwell',
        title='1984',
        year=1949,
        status=True,
    ), TEST_FILE)

    books = BookManager.get_books('1949', TEST_FILE)
    assert len(books) == 1

    books = BookManager.get_books('1984', TEST_FILE)
    assert len(books) == 1

    books = BookManager.get_books('orwell', TEST_FILE)
    assert len(books) == 1

    books = BookManager.get_books(file=TEST_FILE)
    assert len(books) == 1

    books = BookManager.get_books('huxley', TEST_FILE)
    assert len(books) == 0

    FileManager.clear(TEST_FILE)
