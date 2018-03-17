import re

s = 'a = 1'

m = re.search(r'\w', s)
print(m.group())

m = re.match(r'\w', s)
print(m.group())
m = re.fullmatch(r'\w', s)
if m:
    print(m.group())
else:
    print('Ничего не найдено')
