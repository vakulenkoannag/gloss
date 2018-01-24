import random

x = random.randint(0, 10)
print(x)

a = ['cat', 'dog', 'python']
x = random.choice(a)
print(x)
random.shuffle(a)
print(a)
sub_a = random.sample(a, 2)
print(sub_a)

s = 'table'
s1 = random.sample(s, len(s))
s1 = ''.join(s1)
#s1 = ''
#for x in a:
#   s1 += x
print(s1)
