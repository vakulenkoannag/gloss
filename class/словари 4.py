import collections

d = {2: 'He', 3: 'Li', 4: 'Be'}
d[1] = 'H'

print('Случайный порядок')
for k, v in d.items():
    print(k,v)

print('Упорядочено по ключам')
for k in sorted(d):
    print(k, d[k])

print('Упорядочено по значениям')
for k in sorted(d, key=d.get):
    print(k, d[k])

ordered_dict = collections.OrderedDict()
ordered_dict[2] = 'He'
ordered_dict[1] = 'H'
ordered_dict[3] = 'Li'
ordered_dict[4] = 'Be'
print('Соблюден порядок добавления элементов')
for k,v in ordered_dict.item():
    print(k,v)
