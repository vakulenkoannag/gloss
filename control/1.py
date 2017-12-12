with open('Ozhegov.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        no_line_break = line.strip()
        splitted_lines = no_line_break.split('|')
        voc_words = splitted_lines[0]
        if len(voc_words) >= 20:
            print(no_line_break)
