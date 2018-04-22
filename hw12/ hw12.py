import os
import re

def file_list():
    file_list = os.listdir()
    counter = 0
    files_without_numbers = []
    for file in file_list:
        r = re.search('\.[a-z]+', file)
        if r:
            r = re.search('\d', file)
            if not r:
                counter += 1
                files_without_numbers.append(file)
    print('Найдено файлов, не содержащих цифр в названии: ', counter)
    print('Список этих файлов: ')
    print('\n'.join(files_without_numbers))

file_list()
