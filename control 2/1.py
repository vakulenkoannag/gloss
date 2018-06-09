import re

def open_file():
    with open('mystem.xml', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def counter_symbols(text):
    find_part = re.search(r'<body>([\d\D]*?)</body>', text)
    needed_symbols = ''.join(find_part.group(1))
    counted_symbols = len(needed_symbols)
    return counted_symbols

def write_counter(counted_symbols):
    with open('counter.txt', 'w', encoding = 'utf-8') as f:
        f.write('Число символов внутри тега body равно ' + str(counted_symbols))

def final():
    write_counter(counter_symbols(open_file()))
    print('Программа записала ответ в файл counter.txt')

final()
