# можно вечно смотреть на три вещи - огонь, воду и как питон распечатывает миллиард списков. поэтому я оставила в файле семь глав.

import re

def open_file():
    with open('Pride_and_Prejudice_cut.txt', encoding='utf-8') as f:
        text = f.read()
    return text

def clean_everything(text):
    text = text.replace('Mrs.', 'Mrs')
    text = text.replace('Mr.', 'Mr')
    phrases = re.split('[.!?…]+', text)
    clean_phrases = [re.sub('[,:;—–­()&“”«»/*\"\'\n]', '', phrase) for phrase in phrases]
    return clean_phrases

def get_title_words(clean_phrases):
    for clean_phrase in clean_phrases:
        words = clean_phrase.split()
        length = len(words)
        title_words = []
        if length > 10:
            get_title_words = [title_words.append(word) for word in words if word.istitle()]
            print('; '.join(title_words))

def final():
    text = open_file()
    get_title_words(clean_everything(text))

final()
