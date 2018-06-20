import os
import re

# первое задание

def clear_files():
    start_path = './news/'
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
                title = re.search(r'<title>(.+?) // (.+?)</title>', text)
                title = title.group(1) + '\n'
                clear = re.sub(r'<se>', 'абзацкостыль', text)
                clear = re.sub(r'<(.+?)>', '', clear)
                clear = re.sub(r'`', '', clear)
                clear = re.sub(r'\n', ' ', clear)
                clear = re.sub(r'\n+', '', clear)
                clear = re.sub(r'абзацкостыль', '\n', clear)
                clear = re.sub(r'\n+', '\n', clear)
                txt  = '.txt'
                newfile = path + txt
                with open(newfile, 'w', encoding='cp1251') as f_w:
                    f_w.write(title + clear)

clear_files()
