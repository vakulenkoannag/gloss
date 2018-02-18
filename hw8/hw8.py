import random

def makedict():
    with open('words.csv', encoding='utf-8') as f:
        lines = f.readlines()
        dic = {}
        for line in lines:
            no_line_break = line.strip()
            word, hints = no_line_break.split(',')
            hints  = hints.split(' ')
            worddic = dic.setdefault(word, hints)
    return dic

def game():
    chosenword = random.choice(list(makedict().keys()))
    lettercount = []
    for letter in chosenword:
       lettercount .append('.')
    ellipsis = ''.join(lettercount)
    print('Слово загадано. Подсказка:', (makedict()[chosenword][0]), ellipsis)
    userword = input('Введите слово: ')
    if userword == chosenword:
        print('Вы угадали!')
    else:
        print('Подсказка:', makedict()[chosenword][1], ellipsis)
        userword = input('Неправильно! Введите слово: ')
        if userword == chosenword:
            print('Вы угадали!')
        else:
            print('Подсказка:', makedict()[chosenword][2], ellipsis)
            userword = input('Попробуйте еще раз! Введите слово: ')
            if userword == chosenword:
                print('Вы угадали!')
            else:
                print('Подсказка:', makedict()[chosenword][3], ellipsis)
                userword = input('Снова неверно! Введите слово: ')
                if userword == chosenword:
                    print('Вы угадали!')
                else:
                    print('Подсказка:', makedict()[chosenword][4], ellipsis)
                    userword = input('Последняя попытка! Введите слово: ')
                    if userword == chosenword:
                        print('Вы угадали!')
                    else:
                        print('К сожалению, вы проиграли. Загаданное слово:', chosenword)
                    print('Игра окончена.')

def askagain():
    answer = input('Хотите сыграть еще раз? (Ответьте "да" или "нет"): ')
    while answer == 'да':
        game()
        answer = input('Хотите сыграть еще раз? (Ответьте "да" или "нет"): ')
    else:
        print('Игра окончена. До свидания!')

def final():
    print('Добро пожаловать! Игра начинается.')
    game()
    askagain()

final()
