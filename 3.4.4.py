userName, userMath, userPhysics, userRus = [], [], [], []
File = open('C:\\dataset_3363_4.txt')
for line in File.readlines():
	a = line.strip()
	b = a.split(';')
	userName.append(b[0])
	userMath.append(b[1])
	userPhysics.append(b[2])
	userRus.append(b[3])
AverageValueMath, AverageValuePhysics, AverageValueRus = 0, 0, 0
count = 0
for user in range(len(userName)):
	outputAverageValue = ((int(userMath[user]))+(int(userPhysics[user]))+(int(userRus[user])))/3
	count += 1
	AverageValueMath += int(userMath[user])
	AverageValuePhysics += int(userPhysics[user])
	AverageValueRus += int(userRus[user])
	print(outputAverageValue)
print((AverageValueMath/count), (AverageValuePhysics/count), (AverageValueRus/count))
