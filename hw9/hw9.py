import re

def nameinput():
    filename = input('Введите название файла: ')
    return filename

def gettext(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    for symbol in ['.', ',', ':', ';', '—', '!', '?', '*', '&', '"', '"', '«', '»', '…', '/', '(', ')']:
        if symbol in text:
            text = text.replace(symbol, ' ')
    return text

def searchwords(text):
    found = {}
    allforms = ['найтис?ь?\s', 'найд[еёияу][штм]?[еь]?с?[ья]?\s',
            'найден[оаы]?н?[а-я]?[а-я]?[а-я]?\s', 'наш[её]?л[аои]?с?[ья]?\s',
            'нашедш[а-я][а-я]?с?[ья]?\s']
    for form in allforms:
        form_found = re.findall(form, text)
        for word in form_found:
            word = word.strip()
            if word in found:
                found[word] += 1
            else:
                found[word] = 1
    return found

def listforms(found):
    for key, value in found.items() :
        print (key)

def checkfile(filename):
    try:
        with open(filename): pass
    except FileNotFoundError:
        return False

def final():
    filename = nameinput()
    while checkfile(filename) == False:
        print('Такого файла тут нет! Попробуйте ввести другое название.')
        filename = nameinput()
    else:
        print('Список встретившихся в тексте форм глагола «найти»: ')
        listforms(searchwords(gettext(filename)))

final()
