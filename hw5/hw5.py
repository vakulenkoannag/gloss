word = input('Введите слово: ')
all_words = []
while word != '':
    all_words.append(word)
    word = input('Введите еще одно слово: ')
with open('words.txt', 'w', encoding='utf-8') as f:
    for i in enumerate(all_words):
        if len(i[1]) > 5:
           with open('words.txt', 'a', encoding='utf-8') as f:
               f.write(i[1])
               f.write('\n')
