a, f = int(input()), 0
l = [a]
while a != 0:
	b = int(input())
	a += b
	l += [b]
for i in range (len(l)):
	f += l[i]*l[i]
print(f)
#Your code complexity score is 10.86 (best for this step is 1.0).