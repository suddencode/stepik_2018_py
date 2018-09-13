a, b, x, n = int(input()), int(input()), 0, 0
for i in range(a, b +1):
	if i % 3 == 0:
		x += 1
		n += i
print(n/x)
