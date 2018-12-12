n, d = int(input()), {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}
for i in range(n):
    c = input().split()
    d[c[0]] += int(c[1])
print((d['восток'] - d['запад']), (d['север'] - d['юг']))
