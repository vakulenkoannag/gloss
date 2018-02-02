word = input('Введите слово или фразу на русском языке: ')
while word == '':
    word = input('Это пустая строка! Введите слово или фразу на русском языке: ')

for letter in word:
    if letter in 'аеёиоуыэюя':
        letter = letter + 'с' + letter
        print(letter, end = "")
    elif letter in 'АЕЁИОУЫЭЮЯ':
        letter = letter + 'с' + letter.lower()
        print(letter, end = "")
    else:
        print(letter, end = "")
