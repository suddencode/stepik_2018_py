a, b, c, d = int(input()), int(input()), int(input()), int(input())
for n in range (c, d + 1):
	print('\t', n, end='')
print('', end='\n')
for i in range (a, b + 1):
	print(i, '\t',end='')
	for n in range (c, d + 1):
		print(i*n, '\t', end='')
	print('', end='\n')

#Your code complexity score is 19.03 (best for this step is 1.0).
