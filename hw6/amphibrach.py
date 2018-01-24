import random
# эта программа генерирует стихотворение с соблюдением метрической схемы - трехстопный амфибрахий

# составим четверостишие, где будут чередоваться строки с женской и мужской клаузулой:
# - ! - - ! - - ! - 
# - ! - - ! - - !   
# - ! - - ! - - ! - 
# - ! - - ! - - !   
# где "-" - безударный слог, "!" - ударный

# эта фунция выбирает клитик в зависимости от аргумента - контекста

def clitic(context):
    with open('clitics_1.txt', 'r', encoding='utf-8') as f:
        clitics_1 = f.readlines()
    clitic_1 = random.choice(clitics_1)
    with open('clitics_2.txt', 'r', encoding='utf-8') as f:
        clitics_2 = f.readlines()
    clitic_2 = random.choice(clitics_2).replace("\n", "") 
    with open('clitics_3.txt', 'r', encoding='utf-8') as f:
        clitics_3 = f.readlines()
    clitic_3 = random.choice(clitics_3).replace("\n", "") 
    if context == 'noun':
        return random.choice(clitics_1).replace("\n", "")
    elif context == 'place':
        return random.choice(clitics_2).replace("\n", "")
    return random.choice(clitics_3).replace("\n", "")

# все дальнейшие функции не будут иметь аргументов

# verse1

def noun_1():
    with open('nouns_1.txt', 'r', encoding='utf-8') as f:
        nouns_1 = f.readlines()
    return random.choice(nouns_1).replace("\n", "")

def verb_1():
    with open('verbs_1.txt', 'r', encoding='utf-8') as f:
        verbs_1 = f.readlines()
    return random.choice(verbs_1).replace("\n", "")

def place_phrase():
    with open('clitics_place.txt', 'r', encoding='utf-8') as f:
        clitics_place = f.readlines()
    clitic_place = random.choice(clitics_place)
    with open('nouns_place.txt', 'r', encoding='utf-8') as f:
        nouns_place = f.readlines()
    noun_place = random.choice(nouns_place)
    return clitic_place.replace("\n", "") + ' ' + noun_place.replace("\n", "")

# verse2

def adjective_1():
    with open('adjectives_1.txt', 'r', encoding='utf-8') as f:
        adjectives_1 = f.readlines()
    return random.choice(adjectives_1).replace("\n", "")
    
def noun_2():
    with open('nouns_2.txt', 'r', encoding='utf-8') as f:
        nouns_2 = f.readlines()
    noun_2 = random.choice(nouns_2)
    return noun_2.replace("\n", "")

def noun_3():
    with open('nouns_3.txt', 'r', encoding='utf-8') as f:
        nouns_3 = f.readlines()
    noun_3 = random.choice(nouns_3)
    return noun_3.replace("\n", "")

# verse3

def noun_4():
    with open('nouns_4.txt', 'r', encoding='utf-8') as f:
        nouns_7 = f.readlines()
    return random.choice(nouns_7).replace("\n", "")

def verb_2():
    with open('verbs_2.txt', 'r', encoding='utf-8') as f:
        verbs_3 = f.readlines()
    return random.choice(verbs_3).replace("\n", "")

def noun_5():
    with open('nouns_5.txt', 'r', encoding='utf-8') as f:
        nouns_8 = f.readlines()
    return random.choice(nouns_8).replace("\n", "")

# verse4

def adjective_2():
    with open('adjectives_2.txt', 'r', encoding='utf-8') as f:
        adjectives_2 = f.readlines()
    return random.choice(adjectives_2).replace("\n", "")

def noun_6():
    with open('nouns_6.txt', 'r', encoding='utf-8') as f:
        nouns_6 = f.readlines()
    return random.choice(nouns_6).replace("\n", "")

def word():
    with open('words.txt', 'r', encoding='utf-8') as f:
        words = f.readlines()
    return random.choice(words).replace("\n", "")

# verse5

def verb_3():
    with open('verbs_3.txt', 'r', encoding='utf-8') as f:
        verbs_3 = f.readlines()
    return random.choice(verbs_3).replace("\n", "")

def noun_7():
    with open('nouns_7.txt', 'r', encoding='utf-8') as f:
        nouns_8 = f.readlines()
    return random.choice(nouns_8).replace("\n", "")

def noun_8():
    with open('nouns_8.txt', 'r', encoding='utf-8') as f:
        nouns_8 = f.readlines()
    return random.choice(nouns_8).replace("\n", "")

def punctuation():
    with open('punctuation.txt', 'r', encoding='utf-8') as f:
        punctuation = f.readlines()
    return random.choice(punctuation).replace("\n", "")

def verse1():
    # эта функция собирает строчку вида "не ветер бушует над бором!"
    return clitic('noun') + ' ' + noun_1() + ' ' + verb_1() + ' ' + place_phrase() + punctuation()

def verse2():
    # эта функция собирает строчку вида "средь шумного бала - разбойник?"
    return clitic('place') + ' ' + adjective_1() + ' ' + noun_2() + ' — ' + noun_3() + punctuation()

def verse3():
    # эта функция собирает строчку вида "король побеждает пиратов."
    return noun_4() + ' ' + verb_2() + ' ' + noun_5() + punctuation()

def verse4():
    # эта функция собирает строчку вида "ведь русская доля - ему..."
    return clitic('expression') + ' ' + adjective_2() + ' ' + noun_6() + ' — ' + word() + punctuation()

def verse5():
    # эта функция собирает строчку вида "обходит владенья барон."
    return verb_3() + ' ' + noun_7() + ' ' + noun_8() + punctuation()

def make_verse_f():
    # эта функция выбирает случайный номер из 1, 2, 3 (строки с женской клаузулой) и возвращает соответствующую строчку
    verse = random.choice([1,2,3])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()

def make_verse_m():
    # эта функция выбирает случайный номер из 4, 5 (строки с мужской клаузулой) и возвращает соответствующую строчку
    verse = random.choice([4,5])
    if verse == 4:
        return verse4()
    else:
        return verse5()

# этот код распечатывает 4 случайные строчки, чтобы получилась строфа. 
for i in range(2):
    print(make_verse_f())
    print(make_verse_m())
