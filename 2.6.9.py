g, a, x = '', input(), input()
lst = a.split()
for i in range (len(lst)):
	if lst[i] == x:
		g += str(i) + ' '
if g == '':
	print('Отсутствует')
else:
	print(g[:-1])
#Your code complexity score is 11.79 (best for this step is 1.0).