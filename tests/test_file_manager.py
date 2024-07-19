import pytest

from utils.file_manager import FileManager

TEST_FILE = 'test_data/test_data.json'
TEST_ID_FILE = 'test_data/test_latest_id.txt'


def test_read_write_json():
    '''
    Тестирует чтение-запись из файла
    '''
    FileManager.clear(TEST_FILE)

    data = FileManager.read_json(TEST_FILE)
    assert len(data) == 0
    FileManager.write_new_data({
        'id': 1,
        'data': {
            'author': 'Author',
            'title': 'Title',
            'year': 1990,
            'status': True,
        }
    }, TEST_FILE)
    data = FileManager.read_json(TEST_FILE)
    assert len(data) == 1

    FileManager.write_data([{
        'id': 1,
        'data': {
            'author': 'Author',
            'title': 'Title',
            'year': 1990,
            'status': True,
        }
    }], TEST_FILE)
    data = FileManager.read_json(TEST_FILE)
    assert len(data) == 1

    FileManager.clear(TEST_FILE)


def test_generate_id():
    '''
    тестирует генератор id
    '''
    book_id = FileManager.generate_id(TEST_ID_FILE)
    assert book_id == 1
    book_id = FileManager.generate_id(TEST_ID_FILE)
    assert book_id == 2

    with open(TEST_ID_FILE, 'w') as f:
        f.write('')
