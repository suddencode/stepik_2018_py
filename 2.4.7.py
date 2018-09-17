str1, a, tmp = str(input()), 1, ''
str1 += '.'
for i in range(0, len(str1)-1):
	if str1[i] == str1[i+1]:
		a += 1
	if str1[i] != str1[i+1]:
		tmp += str1[i]
		tmp += str(a)
		a = 1
print(tmp)
