games, dictWithResuls, temp = int(input()), {}, []
for i in range(games):
    teamAndGoals = input().split(';')
    temp.append(teamAndGoals[0]), temp.append(int(teamAndGoals[1])), temp.append(teamAndGoals[2]), temp.append(int(teamAndGoals[3]))
    if temp[0] not in dictWithResuls:
        dictWithResuls.update({temp[0]: [0, 0, 0, 0, 0]})
    if temp[2] not in dictWithResuls:
        dictWithResuls.update({temp[2]: [0, 0, 0, 0, 0]})
    if temp[1] > temp[3]:
        for key, value in dictWithResuls.items():
            if key == temp[0]:
                value[0], value[1], value[4] = value[0] + 1, value[1] + 1, value[4] + 3
            if key == temp[2]:
                value[0], value[3], = value[0] + 1, value[3] + 1
    if temp[1] < temp[3]:
        for key, value in dictWithResuls.items():
            if key == temp[2]:
                value[0], value[1], value[4] = value[0] + 1, value[1] + 1, value[4] + 3
            if key == temp[0]:
                value[0], value[3] = value[0] + 1, value[3] + 1
    if temp[1] == temp[3]:
        for key, value in dictWithResuls.items():
            if key == temp[0]:
                value[0], value[2], value[4] = value[0] + 1, value[2] + 1, value[4] + 1
            if key == temp[2]:
                value[0], value[2], value[4] = value[0] + 1, value[2] + 1, value[4] + 1
    temp.clear()
for key, value in dictWithResuls.items():
    print(key, end='')
    print(':', end='')
    print(' '.join([str(i) for i in value]))
#Your code complexity score is 41.3 (best for this step is 18.87).
