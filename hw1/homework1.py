a = int(input())
b = int(input())
c = int(input())

if a * b == c:
    print("Числа a и b в сумме дают c")
else:
    print("Числа a и b в сумме не дают c")
if a == 0:
    print("Число c не является решением линейного уравнения ax + b = 0")
elif (-b) / a == c:
    print("Число c является решением линейного уравнения ax + b = 0")
else:
    print("Число c не является решением линейного уравнения ax + b = 0")