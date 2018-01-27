d = {'English':4, 'Math':3, 'Physic':5} #ключ:значение
print(d['Math'])

d = {1: 'one', 2: 'two', 3: 'three'}
school = {
    '8a': ['Masha', 'Petya'],
    '3b': ['Anna', 'Natasha'],
    'music teacher': 'Oleg Bach',
    }
print(school['3b'][1])
print(school)

empty_dict = {}
dict2 = dict(([1, 'one'], [2, 'two']))
empty_dict2 = dict()
print(dict2)

school['physic teacher'] = 'Michael Stop'
school['music teacher'] = 'Alla Borisovnal'
print(school)

a1 = [1,2,3]
a2 = [4,5]
a = a1 + a2
print(a)

school2 = {
    'physic teacher': 'Alex Queen',
    'PDA teacher': 'Elena Kohl',
    }
print(school2)

school.update(school2)
print(school)
