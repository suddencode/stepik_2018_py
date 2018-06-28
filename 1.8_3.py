X = int(input())
H = int(input())
M = int(input())
calc1 = int((H * 60 + M) + X) #узнаю время в минутах
t1=int(calc1 / 60)
f1=(t1 * 60)
t2=(calc1 - f1)
print(t1)
print(t2)
