with open('Ozhegov.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
    splitted_lines = []
    for line in lines:
        no_line_break = line.strip()
        splitted_lines.append(no_line_break.split('|'))
    i = 0
    for one_line in splitted_lines:
        if one_line[2] != '':
            i += 1
    print('Антонимы есть для такого количества слов:', i)
