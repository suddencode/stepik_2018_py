n1, n2, i3 = float(input()), float(input()), str(input())
if i3 == '+':
    x = n1 + n2
    print(x)
elif i3 == '-':
    x = n1 - n2
    print(x)
elif i3 == '*':
    x = n1 * n2
    print(x)
elif i3 == '/':
    if n2 == 0.0:
        print('Деление на 0!')
    else:
        x = n1 / n2
        print(x)
elif i3 == 'mod':
    if n2 == 0.0:
        print('Деление на 0!')
    else:
        print(n1 % n2)
elif i3 == 'pow':
    print(n1 ** n2)
elif i3 == 'div':
    if n2 == 0.0:
        print('Деление на 0!')
    else:
        print(n1 // n2)
else:
    print('Error')