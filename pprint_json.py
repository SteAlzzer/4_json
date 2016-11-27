import json
import os
from optparse import OptionParser


def load_data(filepath):
    '''
    Функция загрузки данных из json-файла
    Аргументы: filepath - путь к файлу
    '''
    if not os.path.isfile(filepath):
        return None 
    with open(filepath, encoding='utf-8') as json_file:
        data = json.load(json_file) 
        return data




def pretty_print_json(data):
    '''
    Функция красивого вывода json-формата на экран

    Аргументы: data - данные из json файла
    '''
    print(json.dumps(data, indent='  ', ensure_ascii=False))

if __name__ == '__main__':
    usage = 'Usage: %prog -p path_to_json'
    parser = OptionParser(usage=usage)

    parser.add_option('-p', '--path', action='store', type='string', help='Путь до json-файла')
    
    options, arguments = parser.parse_args()

    if options.path:
        path = options.path
    else:
        print('Необходимо указать путь до json-файла')
        exit(-1)

    json_data = load_data(path)

    if json_data is None:
        print('Джонни, у нас проблема с файлом. Так дело не пойдёт')
        exit(-1)

    pretty_print_json(json_data)
