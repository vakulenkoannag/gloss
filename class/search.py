import re

s = """
a = 1
b = 4.545
c = .345
d = -24
G = 2*pi*a
"""

m = re.search( # only first sovpadenie
#    r'^[a-zA-Z]+\s*=\s*-?\d+(?:\.\d+)?$',
    r'^(\w+)\s*=\s*(-?\d+(?:\.\d+)?)$',
    s,
    re.MULTILINE
)
print(m.group())
print(m.groups())
print(m.start())
print(m.end())
print(s[m.start():m.end()])

# search - первая встречающаяся подстрока
# findall - все встречающиеся подстроки
# fullmatch - должна соответствовать вся строка целиком
# match - работает, если соответствует начало строки
