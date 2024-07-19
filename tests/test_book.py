import pytest

from utils.book import Book


@pytest.fixture()
def book():
    return Book('Title', 'Author', 1990)


def test_init(book):
    assert book.title == 'Title'
    assert book.author == 'Author'
    assert book.year == 1990


def test_str(book):
    assert book.__str__() == 'Author - Title (1990)'
