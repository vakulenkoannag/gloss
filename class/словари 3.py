#fname = print(input('Введите название файла: '))

import collections

def words_from_text(fname):
    with open(fname, encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    symbols_to_remove = """,.:;()-–?!*"""
    for s in symbols_to_remove:
        text = text.replace(s, '')
    words = text.split()
    return words

def word_count(words):
    count = {}
    for x in words:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    for k, v in count.items():
        count[k] = v / len(words)
    return count

def most_popular(count, n):
    words = sorted(count, key=count.get, reverse=True)
    return words[:n]




words = words_from_text('dochka.txt')
#print(words[:20])
count = word_count(words)
#print(count['пугачев'])
print(most_popular(count, 20))

counter = collections.Counter(words)
print(counter.most_common(20))
