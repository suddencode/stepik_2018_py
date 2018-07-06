a, b, c = int(input()), int(input()), int(input())
if a <= b <= c and a <= c :
    print(c, a, b, sep = "\n")
elif a <= b >= c and a <= c :
    print(b, a, c, sep = "\n")
elif a >= b <= c and a <= c :
    print(c, b, a, sep = "\n")
elif a <= b >= c and a >= c:
    print(b, c, a, sep = "\n")
elif a >= b <= c and a >= c:
    print(a, b, c, sep = "\n")
elif a >= b >= c and a >= c:
    print(a, c, b, sep = "\n")
else:
    pass