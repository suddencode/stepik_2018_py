Y = int(input())
if Y % 4 == 0 and not Y % 100 == 0 or Y % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
#Your code complexity score is 6.48 (best for this step is 1.0).