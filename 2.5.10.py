a = str(input())
b = a.split()
if len(b) == 1:
	print(a)
else:
	for i in range (len(b)-1):
	    print(int(b[1+i]) + int(b[-1+i]), end=' ')
	print(int(b[0]) + int(b[-2]))

#Your code complexity score is 15.26 (best for this step is 1.0).
