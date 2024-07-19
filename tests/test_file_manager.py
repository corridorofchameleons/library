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
    FileManager.write_data('new_data', TEST_FILE)
    data = FileManager.read_json(TEST_FILE)
    assert len(data) == 1
