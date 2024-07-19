import json

FILE = 'data/data.json'
ID_FILE = 'data/latest_id.txt'


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
    def write_new_data(new_data, file=FILE):
        '''
        записывает в файл
        '''
        data = FileManager.read_json(file)
        data.append(new_data)
        with open(file, 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    @staticmethod
    def write_data(data, file=FILE):
        with open(file, 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    @staticmethod
    def clear(file=FILE):
        '''
        очищает файл
        '''
        with open(file, 'w') as f:
            data = []
            json.dump(data, f, ensure_ascii=False)

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
