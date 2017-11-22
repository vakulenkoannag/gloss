with open('sonnet_130.txt', encoding = 'utf-8-sig') as f:
    text = f.read()
lines = text.splitlines()
minimum = len(lines[0].replace("\n", ""))
maximum = len(lines[0].replace("\n", ""))
for line in lines:
    if len(line) > maximum:
        maximum = len(line)
    if len(line) < minimum and len(line) != 0:
        minimum = len(line)
if minimum == maximum:
    print('В этом документе все строки равны.')
else:
    print('В этом документе самая короткая строка короче самой длинной в', round(maximum / minimum, 2), 'раз(а).')
