d, count, file = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,'11': 0}, {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,'11': 0}, open('C:\\Users\\py\\Downloads\\dataset_3380_5.txt')
for line in file.readlines():
	a = line.strip().split('\t')
	d[str(a[0])] += float(a[2])
	count[str(a[0])] += 1
for key in d:
	if d[key] != 0:
		print(key, float(d[key])/count[key])
	if d[key] == 0:
		print(key, '-')
