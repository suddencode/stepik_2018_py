def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    if key not in d:
        if 2 * key in d:
            d[key*2] += [value]
        else:
            d[key*2] = [value]
    return d
d = {}
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
#Your code complexity score is 6.4 (best for this step is 2.45).