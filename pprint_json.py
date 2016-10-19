import json
import os
from optparse import OptionParser

#################################
# Обращение к господину ведущему:
#################################
# Осознаю, что алгоритм весьма костыльный и вообще. По этому и вопрос: в какую сторону копать?
# Как корректно выводить запятые?
# Как корректно выводить открывающие скобки в случае * (будет понятно дальше по тексту)?


def load_data(filepath):
    '''
    Функция загрузки данных из json-файла
    Аргументы: filepath - путь к файлу
    '''
    if not os.path.isfile(filepath):
        return None # Если файла не существует, или по пути расположен не файл, то выходим из функции
    with open(path, encoding='utf-8') as json_file:
        line = json_file.read() # Читаем всю дичь из файла
    data = json.loads(line) # Интерпретируем всю дичь из файла в json-формат с помощью модуля json
    return data

def print_with_tab(string, tab_size, tab_char='    ', end=True):
    '''
    Функция для вывода на экран переданной строки с учётом вложенности (отступами)
    Аргументы:  string - сама строка (str)
                tab_size - уровень отсупа (int)
                tab_char - символ табуляции для отступа (str)
                end - используется для печати следующего значения на этой же строке (bool)
    '''
    # Зачем-то проверяем все передаваемые значения
    assert type(tab_size) == int and tab_size > 0, 'size should be int and greater that 0'
    assert type(tab_char) == str, 'tab_char should be string and nothing else'
    
    print(tab_char*tab_size, end='') # Выводим необходимое количество отступов
    
    if end: # Переводим строку на новую
        print(string)
    else: # Не переводим строку на новую
        print(string, end='')

def print_json_data(data, tab_size=1, suspend_first_tab=False, how_about_coma=False):
    '''
    Рекурсивно-вызываемая функция для прелестнейшего вывода на экран формата json.
    Аргументы:  data - сами данные в формате json
                tab_size - уровень отступа (вложенности)
                suspend_first_tab - флаг, указывающий на вывод самых первых табов для открывающих скоб *
                how_about_coma - флаг, укзывающий на вывод завершающей запятой **

    * На случай, если выводится название поля, а за ним сразу открывающая скоба (например, `"greatItemName" : [`)
    ** На случай, если после закрывающей скобки необходимо вывести запятую, т.к. это не крайний элемент списка-родителя
    '''

    # Определяем тип переданного элемента. В зависимости от этого выводим соответсвующую скобу.
    if type(data) == list:
        if suspend_first_tab: # Это используется на случай, если выводить отсупы не нужно *
            print('[')
        else:
            print_with_tab('[', tab_size)
            tab_size += 1 # Увеличиваем отступ

        for item_num, item in enumerate(data): # Перебираем элементы
            # Определяем тип элемента в листе. Если строка или число, то сразу выводим на экран.
            if type(item) == int or type(item) == float:
                if item_num != len(data)-1: # Данная конструкция определяет, последний это элемент списка или нет.
                    print_with_tab('{},'.format(item), tab_size) # Если нет, выводит в конце запятую
                else:
                    print_with_tab('{}'.format(item), tab_size)
            elif type(item) == str:
                if item_num != len(data)-1:
                    print_with_tab('"{}",'.format(item), tab_size)
                else:
                    print_with_tab('"{}"'.format(item), tab_size)
            # Если тип элемента не строка или число, вызываем нашу любимую рекурсию
            else:
                if item_num != len(data)-1: # Если текущий элемент списка не последний, выводим запятую у скобы в рекурсивно-вызываемой функции (случай **)
                    print_json_data(item, tab_size+1, how_about_coma=True)
                else:
                    print_json_data(item, tab_size+1)

    elif type(data) == dict:
        # Работаем аналогично случаю с листом
        if suspend_first_tab:
            print('{')
        else:
            print_with_tab('{', tab_size)
            tab_size += 1

        for item_num, item_key in enumerate(data): # Перебираем ключи словаря
            item_value = data[item_key] # Сразу определяем значение по ключу
            item_type = type(item_value) # И тип этого элемента
            # Так же, как и выше, обрабатываем типы:
            if item_type == int or item_type == float: # Если можем вывести - выводим
                if item_num != len(data)-1:
                    print_with_tab('"{}" : {},'.format(item_key, item_value), tab_size)
                else:
                    print_with_tab('"{}" : {}'.format(item_key, item_value), tab_size)
            elif item_type == str: # Если можем вывести - выводим
                if item_num != len(data)-1:
                    print_with_tab('"{}" : "{}",'.format(item_key, item_value), tab_size)
                else:
                    print_with_tab('"{}" : "{}"'.format(item_key, item_value), tab_size)
            elif item_type == dict or item_type == list:  # Если нет - запускаем рекурсию на элементе словаря
                print_with_tab('"{}" : '.format(item_key), tab_size, end=False) # Только вначале выводим название ключа (как раз случай для *)
                if item_num != len(data)-1: # Если текущий элемент словаря не последний, выводим запятую у скобы в рекурсивно-вызываемой функции (случай **)
                    print_json_data(data[item_key], tab_size+1, suspend_first_tab=True, how_about_coma=True) # А также ещё важно подавить вывод отступов *
                else:
                    print_json_data(data[item_key], tab_size+1, suspend_first_tab=True)
            else: # Обработка NoneType
                if item_num != len(data)-1:
                    print_with_tab('"{}" : null,'.format(item_key), tab_size)
                else:
                    print_with_tab('"{}" : null'.format(item_key), tab_size)

    tab_size -= 1 # Коль закончили вывод всех элементов на текущем уровне вложенности, то самое время его уменьшить
    if type(data) == list:
        if how_about_coma:
            print_with_tab('],', tab_size)
        else:
            print_with_tab(']', tab_size)
    elif type(data) == dict:
        if how_about_coma:
            print_with_tab('},', tab_size)
        else:
            print_with_tab('}', tab_size)

def pretty_print_json(data):
    '''
    Функция красивого вывода json-формата на экран

    Аргументы: data - данные из json файла
    '''
    print_json_data(data) # Запускаем рекурсивную функцию


if __name__ == '__main__':
    usage = 'Usage: %prog -p path_to_json'
    parser = OptionParser(usage=usage)

    parser.add_option('-p', '--path', action='store', type='string', help='Путь до json-файла')
    
    options,arguments=parser.parse_args()
    options = options.__dict__

    if options['path']:
        path = options['path']
    else:
        print('Необходимо указать путь до json-файла')
        exit(-1)

    json_data = load_data(path)

    if json_data is None:
        print('Джонни, у нас проблема с файлом. Так дело не пойдёт')
        exit(-1)

    pretty_print_json(json_data)
