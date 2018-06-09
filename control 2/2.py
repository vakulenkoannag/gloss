import re

def open_file():
    with open('mystem.xml', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

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

def final():
    write_gr_tags(make_dict(open_file()))
    print('Программа записала ответ в файл gr_tags_sorted.txt')

final()
