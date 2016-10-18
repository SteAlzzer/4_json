import json
import os
from optparse import OptionParser


def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(path, encoding='utf-8') as json_bar_file:
        line = json_bar_file.read()

    bars = json.loads(line)
    return bars

def print_with_tab(string, tab_size, tab_char='\t'):
    assert type(tab_size) == int and tab_size > 0, 'size should be int and greater that 0'
    assert type(tab_char) == str, 'tab_char should be string and nothing else'
    print(tab_char*tab_size, end='')
    print(string)

def pretty_print_json(data, tab_size=1):
    # tab_size = 1
    if type(data) == list:
        print_with_tab('[', tab_size)
    elif type(data) == dict:
        print_with_tab('{', tab_size)
    tab_size += 1

    for item in data:
        if type(item) == list:
            print_with_tab('[', tab_size)
        elif type(item) == dict:
            print_with_tab('{', tab_size)
        tab_size += 1
        for item_key in item:
            item_value = item[item_key]
            item_value_type = type(item_value)
            if item_value_type == int:
                print_with_tab('"{}" : {}'.format(item_key, item_value), tab_size)
            elif item_value_type == str:
                print_with_tab('"{}" : "{}"'.format(item_key, item_value), tab_size)
            elif item_value_type == list:
                pass
            elif item_value_type == dict:
                pass
            else:
                print('Wooow. Unknown type detected: {}:{} is {}'.format(item_key, item_value, item_value_type))
            # print_with_tab(item_key, tab_size)
        tab_size -= 1
        if type(item) == list:
            print_with_tab(']', tab_size)
        elif type(item) == dict:
            print_with_tab('}', tab_size)

    tab_size -= 1
    if type(data) == list:
        print_with_tab(']', tab_size)
    elif type(data) == dict:
        print_with_tab('}', tab_size)

if __name__ == '__main__':
    usage = 'Usage: %prog -p path_to_json'
    parser = OptionParser(usage=usage)

    parser.add_option('-p', '--path', action='store', type='string', help='Путь до json-файла')
    
    options,arguments=parser.parse_args()
    options = options.__dict__

    if options['path']:
        path = options['path']
    else:
        print('Необходимо указать путь до файла с барами в json')
        exit(-1)

    json_data = load_data(path)

    if json_data is None:
        print('Джонни, у нас проблема с файлом')
        exit(-1)

    pretty_print_json(json_data)