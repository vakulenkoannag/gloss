def nameinput():
    filename = input('Введите название файла: ')
    return filename

def getwords(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    for symbol in ['.', ',', ':', ';', '—', '!', '?', '*', '&', '"', '"', '«', '»', '…', '/', '(', ')']:
        if symbol in text:
            text = text.replace(symbol, ' ')
            # replace на пробел, потому что в текстовом файле кое-где нет пробелов в сочетании "слово знак препинания слово" и два слова слипаются в одно.
            # такое, думаю, может случиться в любом файле, а не только в данном для примера.
    wordsfromtext = text.split()
    return wordsfromtext

def dictionary(wordsfromtext):
    dictionary = {}
    for word in wordsfromtext:
        if word.endswith('ness'):
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return dictionary

def count(dictionary):
    count = 0
    for word in dictionary:
        count += dictionary[word]
    return count

def mostpopular(dictionary):
    wordsfromtext = sorted(dictionary, key=dictionary.get, reverse=True)
    return wordsfromtext[0]

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
        print('Всего в тексте разных существительных с суффиксом «ness»:', count(dictionary(getwords(filename))),
        '\nИз них максимальную частотность имеет:', mostpopular(dictionary(getwords(filename))))

final()
