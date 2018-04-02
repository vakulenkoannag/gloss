import re

def nameinput():
    filename = input('Введите название файла: ')
    return filename

def gettext(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def searchstring(text):
    search = re.search(r'Часовой пояс[^\n]+\n([^\n]+\n)', text)
    timezonestring = search.group(1)
    return timezonestring

def gettimezone(timezonestring):
    findall = re.findall('>([^<>]+)<', timezonestring)
    timezone = ''.join(findall)
    return timezone

def getstate(text):
    search = re.search('<title>([а-яА-Я]+)\s', text)
    state = search.group(1)
    return state

def writefile(state, timezone):
    finalstring = 'Часовой пояс в городе ' + state + ' — ' + timezone
    with open('timezone.txt', 'w', encoding='utf-8') as f:
        f.write(finalstring)

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
        print('Часовой пояс этого города записан в текстовом файле "timezone.txt".')
        state = getstate(gettext(filename))
        timezone = gettimezone(searchstring(gettext(filename)))
        writefile(state, timezone)

final()
