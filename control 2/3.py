import re

def open_file():
    with open('mystem.xml', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

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
        
def final():
    write_file(verbs(open_file()))
    make_csv(open_file())
    print('Программа записала ответ в файл verbs_counter.txt и создала файл mystem.csv')

final()
