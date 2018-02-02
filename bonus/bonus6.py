def isfloat(value):
    try:
        float(value)
        return float(value)
    except (TypeError, ValueError):
        return False

height = isfloat(input('Введите рост в см: '))
while height == False:
    height = isfloat(input('Рост должен быть числом больше нуля!Введите рост в см: '))

weight = isfloat(input('Введите вес в кг: '))
while weight == False:
    weight = isfloat(input('Вес должен быть числом больше нуля!Введите вес в кг: '))

BMI = round((weight/((height/100)**2)), 2)

if BMI <= 16:
    print ('Выраженный дефицит массы тела')
elif BMI < 18.5:
    print ('Недостаточная (дефицит) масса тела')
elif BMI <= 24.99:
    print ('Норма')
elif BMI < 30:
    print ('Избыточная масса тела (предожирение)')
elif BMI < 35:
    print ('Ожирение первой степени')
elif BMI < 40:
    print ('Ожирение второй степени')
elif BMI >= 40:
    print ('Ожирение третьей степени (морбидное)')
