d, mySet1, mySet2 = int(input()), set(), set()
for i in range(d):
	tmp = input()
	mySet1.add(tmp.lower())
l = int(input())
for g in range(l):
	input_str = input()
	input_str = input_str.lower().split()
	for k in range(len(input_str)):
		mySet2.add(input_str[k])
out = list(mySet2 - mySet1)
for j in range(len(out)):
	print(out[j])