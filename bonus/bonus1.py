number = input('Введите число: ')
numbers = []
amount = 0
total = 0

while number != '':
    numbers.append(float(number))
    number = input('Введите число ещё одно число: ')

for number in numbers:
    amount += 1
    total += number

print('Среднее арифметическое введённых чисел: ', total/amount,
      '\nМинимальное из введённых чисел: ', min(numbers),
      '\nМаксимальное из введённых чисел: ', max(numbers))
