import json
import os
from optparse import OptionParser


def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(path, encoding='utf-8') as json_file:
        line = json_file.read()

    data = json.loads(line)
    return data

def print_with_tab(string, tab_size, tab_char='    ', end=True):
    assert type(tab_size) == int and tab_size > 0, 'size should be int and greater that 0'
    assert type(tab_char) == str, 'tab_char should be string and nothing else'
    print(tab_char*tab_size, end='')
    if end:
        print(string)
    else:
        print(string, end='')

def pretty_print_json(data, tab_size=1, suspend_first_tab=False, how_about_coma=False):
    if type(data) == list:
        if suspend_first_tab:
            print('[')
        else:
            print_with_tab('[', tab_size)
            tab_size += 1
        for item_num, item in enumerate(data):
            # print('helllooo\t{}'.format(type(item)))
            if type(item) == int or type(item) == float:
                if item_num != len(data)-1:
                    print_with_tab('{},'.format(item), tab_size)
                else:
                    print_with_tab('{}'.format(item), tab_size)
            elif type(item) == str:
                if item_num != len(data)-1:
                    print_with_tab('"{}",'.format(item), tab_size)
                else:
                    print_with_tab('"{}"'.format(item), tab_size)
            else:
                # print_with_tab('"{}" : '.format(item), tab_size, end=False)
                if item_num != len(data)-1:
                    pretty_print_json(item, tab_size+1, how_about_coma=True)
                else:
                    pretty_print_json(item, tab_size+1)
            # else:
            #     print_with_tab('"{}" : null'.format(item), tab_size)
            # pretty_print_json(item, tab_size+1)
    elif type(data) == dict:
        if suspend_first_tab:
            print('{')
        else:
            print_with_tab('{', tab_size)
            tab_size += 1
        for item_num, item_key in enumerate(data):
            item_value = data[item_key]
            item_type = type(item_value)
            if item_type == int or item_type == float:
                if item_num != len(data)-1:
                    print_with_tab('"{}" : {},'.format(item_key, item_value), tab_size)
                else:
                    print_with_tab('"{}" : {}'.format(item_key, item_value), tab_size)
            elif item_type == str:
                if item_num != len(data)-1:
                    print_with_tab('"{}" : "{}",'.format(item_key, item_value), tab_size)
                else:
                    print_with_tab('"{}" : "{}"'.format(item_key, item_value), tab_size)
            elif item_type == dict or item_type == list:
                print_with_tab('"{}" : '.format(item_key), tab_size, end=False)
                if item_num != len(data)-1:
                    pretty_print_json(data[item_key], tab_size+1, suspend_first_tab=True, how_about_coma=True)
                else:
                    pretty_print_json(data[item_key], tab_size+1, suspend_first_tab=True)
            else:
                if item_num != len(data)-1:
                    print_with_tab('"{}" : null,'.format(item_key), tab_size)
                else:
                    print_with_tab('"{}" : null'.format(item_key), tab_size)

    tab_size -= 1
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


    # print('==============')
    # print('{', end='')
    # # print()
    # print('==============')