word = input()
for i, letter in enumerate(word):
    if i % 2 == 0 and letter in 'опе':
        print(letter)
