def f(x):
    if x <= -2:
        r1 = 1 - (x + 2)**2
        return r1
    if -2 < x <= 2:
        r2 = -x / 2
        return r2
    if 2 < x:
        r3 = (x-2)**2 + 1
        return r3
#Your code complexity score is 7.81 (best for this step is 4.12).