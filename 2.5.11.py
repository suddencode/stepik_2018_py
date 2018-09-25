a, c = str(input()), []
b = a.split()
x = b.sort()
for i in range (len(b)):
	if b.count(b[i]) > 1:
		if b[i] in c:
			pass
		else:
			c.append(b[i])
d = ' '.join(c)
print(d)

#Your code complexity score is 13.0 (best for this step is 1.0).
