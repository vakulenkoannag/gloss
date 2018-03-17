import re

s1 = 'Hello    World'
s2 = 'Hello,,,,World'
print(s1.split())
print(re.split(r'\s+', s1))
print(s1.split(' '))
print(s2.split(','))
print(re.split(r',+', s2))
