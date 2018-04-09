import re

def openfile():
    with open ('vikings.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def replace(text):
    replaced = re.sub(r'Ви(.?)кинг([уеао]?[мвх]?и?)([\WИ])', r'Бурундук\2\3', text) # И - потому что там в одном месте Викинги с Историей склеились
    replaced = re.sub(r'ви(.?)кинг([уеао]?[мвх]?и?)(\W)', r'бурундук\2\3', replaced)
    return replaced

def writefile(replaced):
    with open('chimpunks.txt', 'w', encoding='utf-8') as f:
        f.write(replaced)

def final():
    text = openfile()
    writefile(replace(text))
    print('Наслаждайтесь исправленной статьёй в файле chimpunks.txt!')

final()
