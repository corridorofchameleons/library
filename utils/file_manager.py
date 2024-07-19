import json

FILE = '../data/data.json'
ID_FILE = '../data/latest_id.txt'


class FileManager:
    '''
    Класс извлечения и записи данных
    '''

    @staticmethod
    def read_json(file=FILE):
        '''
        читает файл
        '''
        with open(file, 'r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def write_data(new_data, file=FILE):
        '''
        записывает в файл
        '''
        data = FileManager.read_json()
        data.append(new_data)
        with open(file, 'w') as f:
            f.write(data)

    @staticmethod
    def generate_id(file=ID_FILE):
        '''
        генерирует идентификатор
        '''
        with open(file, 'r') as f:
            book_id = f.readline()
            book_id = 1 if not book_id else int(book_id) + 1
        with open(file, 'w') as f:
            f.write(str(book_id))
        return book_id


jm.read_json()
jm.generate_id()
