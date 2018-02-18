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

def ellipsis(chosenword):
    lettercount = []
    for letter in chosenword:
       lettercount.append('.')
    ellipsis = ''.join(lettercount)
    return ellipsis

def game():
    chosenword = random.choice(list(makedict().keys()))
    print('Слово загадано. Первая подсказка:', (makedict()[chosenword][0]), ellipsis(chosenword))
    userword = input('Введите слово: ')
    if userword == chosenword:
        print('Вы угадали!')
    else:
        print('Неправильно! Вторая подсказка:', makedict()[chosenword][1], ellipsis(chosenword))
        userword = input('Введите слово: ')
        if userword == chosenword:
            print('Вы угадали!')
        else:
            print('Попробуйте еще раз! Третья подсказка:', makedict()[chosenword][2], ellipsis(chosenword))
            userword = input('Введите слово: ')
            if userword == chosenword:
                print('Вы угадали!')
            else:
                print('Снова неверно! Четвертая подсказка:', makedict()[chosenword][3], ellipsis(chosenword))
                userword = input('Введите слово: ')
                if userword == chosenword:
                    print('Вы угадали!')
                else:
                    print('Мимо! Последняя подсказка:', makedict()[chosenword][4], ellipsis(chosenword))
                    userword = input('Введите слово: ')
                    if userword == chosenword:
                        print('Вы угадали!')
                    else:
                        print('К сожалению, вы проиграли. Загаданное слово:', chosenword)

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
