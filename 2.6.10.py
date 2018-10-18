w, my_list_1 = 0, []
while w == 0:
    row_input = input().split()
    if row_input == ['end']:
        w = 666
        break
    for i in range(len(row_input)):
        row_input[i] = int(row_input[i])
    my_list_1.append(row_input)
for i in range (len(my_list_1)):
    if i > 0:
        print(end='\n')
    for j in range (len(my_list_1[0])):
        print(my_list_1[i][(j-1)%len(my_list_1[i])] + my_list_1[i][(j+1)%len(my_list_1[i])] + my_list_1[(i-1)%len(my_list_1)][j] + my_list_1[(i+1)%len(my_list_1)][j], end='')
        if len(my_list_1[i]) > j+1:
            print(' ', end='')
