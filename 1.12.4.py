n1 = str(input())
if n1 == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c)/2)
    s = (((p*(p-a)*(p-b)*(p-c)))**0.5)
    print(float(s))
elif n1 == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = (a * b)
    print(float(s))
elif n1 == 'круг':
    r = int(input())
    s = 3.14*(r ** 2)
    print(float(s))
else:
    print('Ошибка')
#Your code complexity score is 26.7 (best for this step is 1.0).