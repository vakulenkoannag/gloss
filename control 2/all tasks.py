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

def final_1():
    write_counter(counter_symbols(open_file()))
    print('Ответ на первое задание программа записала ответ в файл counter.txt')

def make_dict(text):
    dictionary = {}
    gr_tags = re.findall(r'gr=\"([\d\D]*?)\"', text)
    for gr_tag in gr_tags:
        if gr_tag in dictionary.keys():
            dictionary[gr_tag] += 1
        else:
            dictionary[gr_tag] = 1
    return dictionary

def write_gr_tags(dictionary):
    with open('gr_tags_sorted.txt', 'w') as f:
        for gr_tag in sorted(dictionary, key=dictionary.get, reverse=True):
            line = gr_tag + '\n'
            f.write(line)

def final_2():
    write_gr_tags(make_dict(open_file()))
    print('Ответ на второе задание программа записала ответ в файл gr_tags_sorted.txt')

def verbs(text):
    counter = 0
    tags = re.findall(r'<w>[\d\D]*?</w>', text)
    for tag in tags:
        if ',сов' in tag or 'сов,' in tag and 'несов' not  in tag:
            if ',ед' in tag or 'ед,' in tag:
#                word = re.findall(r'>([а-яА-Я]+)<', tag)
#                print(word)
                counter += 1
    return counter

def write_file(counter):
    with open('verbs_counter.txt', 'w') as f:
        f.write('Число глаголов совершенного вида в единственном числе: ')
        f.write(str(counter))

def make_csv(text):
    body = re.findall(r'<body>([\d\D]*)</body>', text)
    body = ''.join(body)
    words = re.findall(' lex=\"([а-яА-Я]*)\" gr=\"([\d\D]*?)\" />([а-яА-Я]+)<', body)
    writing = open ('mystem.csv', 'w')
    for word in words:
        line = word[0] + ',' + word[1] + ',' + word[2] + '\n'
        writing.write(line)

def final_3():
    write_file(verbs(open_file()))
    make_csv(open_file())
    print('Ответ на третье задание программа записала ответ в файл verbs_counter.txt  и создала файл mystem.csv')

def final():
    final_1()
    final_2()
    final_3()

final()
