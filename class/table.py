import random

def anno(word):
    a = random.sample(word, len(word))
    new_word = ''.join(a)
    return new_word

with open('text.txt', encoding = 'utf-8') as f:
    text = f.read()
text = text[1:]
text = text.replace(',', '')
text = text.replace('.', '').replace('—', '')
words = text.split()
print(words)

with open('table.csv', 'w') as f:
    for x in words:
        list_line = [x]
        for i in range (3):
            list_line.append(anno(x))
        line = ';'.join(list_line)
        f.write(line)
        f.write('\n')





#    lines = f.readlines()
#    print(lines)
#    words = []
#    for line in lines:
#        no_line_break = line.strip()
#        words.append(no_line_break)
#    print(no_line_break)
