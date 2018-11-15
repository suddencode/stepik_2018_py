import sys
my_list = []
my_list += sys.argv
print(*my_list[1::1])
