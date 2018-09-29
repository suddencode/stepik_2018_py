a, b = int(input()), []
if a == 1:
        print(a)
else:
	for i in range (a + 1):
		b += [i] * i
	c = b[0:a]
	d = ' '.join(str(x) for x in c)
	print(d)
#Your code complexity score is 10.05 (best for this step is 1.0).