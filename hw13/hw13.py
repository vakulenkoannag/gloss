import re
import os

def counter_for_dirs():
    counter = 0
    start_path = os.getcwd()
    for root, dirs, files in os.walk(start_path):
        for dir in dirs:
            if re.match('^[а-яА-Я]*$', dir):
                counter += 1
                print(dir)
    return counter

def final():
    counter = counter_for_dirs()
    print('Количество папок в дереве с полностью кириллическим названием - ', counter)

final()
