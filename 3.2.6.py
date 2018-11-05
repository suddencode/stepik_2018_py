input_str = input()
my_set = set(input_str.lower().split())
for i in my_set:
    print(i, input_str.lower().split().count(i))
#Your code complexity score is 9.22 (best for this step is 1.0).