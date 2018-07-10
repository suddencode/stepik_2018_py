n = str(input())
a, b, c, d, e, f = n[0], n[1], n[2], n[3], n[4], n[5]
a1, b1, c1, d1, e1, f1 = int(a), int(b), int(c), int(d), int(e), int(f)
if a1 + b1 + c1 == d1 + e1 + f1:
    print('Счастливый')
else:
    print('Обычный')