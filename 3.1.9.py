def modify_list(l):
    b = []
    for i in range (len(l)):
        if l[i] % 2 == 0:
            b.append(l[i]//2)
    l.clear()
    for j in range (len(b)):
        l.append(b[j])
#Your code complexity score is 10.1 (best for this step is 2.24).