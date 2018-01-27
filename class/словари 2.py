d = {2: 'He', 3: 'Li', 4: 'Be'}
d[1] = 'H'

print(list(d.keys()))

print('Перебор ключей')
for key in d:
    print(key, d[key])
keys = list(d.keys())

print('Перебор значений')
for value in d.values():
    print(value)
values = list(d.values())

print('Перебор пар')
for key, value in d.items():
    print(key, value)

