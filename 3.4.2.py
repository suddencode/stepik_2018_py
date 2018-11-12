with open('C:\\test.txt') as inf:
	input1 = inf.readline()
out = ''
symb = ''
i = 0
while i != len(input1):
    if not ('0' <= input1[i] <= '9'):
        symb = input1[i]
        i += 1
    if ('0' <= input1[i] <= '9'):
        num = ''
        c = 0
        while ('0' <= input1[i + c] <= '9'):
            num += str(input1[i + c])
            c += 1
            if (i + c) >= len(input1):
                break
        i += c
        out += symb * int(num)
test1 = open('C:\\out.txt', 'w')
test1.write(out)
test1.close()

