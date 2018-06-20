import os
import re

# второе задание

def count_nouns():
    dic = {}
    start_path = './news/'
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
                nouns = re.findall(r'lex="([а-яА-я]+)" gr="S', text)
                for noun in nouns:
                    noun = noun.title()
                    if noun in dic.keys():
                        dic[noun] += 1
                    else:
                        dic[noun] = 1
    with open('nouns.csv', 'w', encoding='utf-8') as f:
        for key in dic.keys():
            value = str(dic[key])
            f.write(key + '\t' + value + '\n')

count_nouns()
