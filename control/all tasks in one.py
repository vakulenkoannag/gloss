# 2 вариант
with open('Ozhegov.txt', encoding = 'utf-8') as f:
# 1 задание
    print('Первое задание: \n')
    lines = f.readlines()
    for line in lines:
        no_line_break = line.strip()
        splitted_lines = no_line_break.split('|')
        voc_words = splitted_lines[0]
        if len(voc_words) >= 20:
            print(no_line_break)
# 2 задание
    print('\nВторое задание: \n')
    splitted_lines = []
    for line in lines:
        no_line_break = line.strip()
        splitted_lines.append(no_line_break.split('|'))
    i = 0
    for one_line in splitted_lines:
        if one_line[2] != '':
            i += 1
    print('Антонимы есть для такого количества слов:', i, '\n')
# 3 задание
    print('Третье задание: \n')
    word = input('Введите слово: ')
    all_words = []
    while word != '':
        all_words.append(word)
        word = input('Введите еще одно слово: ')
    for word in all_words:
        log = True
        for one_line in splitted_lines:
            if word == one_line[0]:
                print(word, ' — ', one_line[1], ' — ', one_line[3])
                log = False
        if log == True:
            print('Слово "', word, '" не нашлось в словаре.')
