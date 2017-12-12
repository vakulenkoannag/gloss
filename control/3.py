with open('Ozhegov.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
    splitted_lines = []
    for line in lines:
        no_line_break = line.strip()
        splitted_lines.append(no_line_break.split('|'))
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
