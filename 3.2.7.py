def f(x):
    return x*10
my_dictionary, n1 = dict(), int(input())
for i in range (n1):
    n2 = int(input())
    if n2 in my_dictionary:
        print(my_dictionary[n2])
    else:
        my_dictionary[n2] = f(n2)
        print(my_dictionary[n2])

# Your code complexity score is 11.58 (best for this step is 1.0).