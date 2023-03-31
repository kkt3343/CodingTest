#input = "ULURRDLLULDR"
input = "LULLLLLLU"

import re
separators = "L", "R", "D", "U"

def custom_split(sepr_list, str_to_split):
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, str_to_split)

def cal(point1, point2):
    if point1[0] >= 5 and point2[0] == 1:
        point1[0] = point1[0] - 1
    elif point1[0] <= -5 and point2[0] == -1:
        point1[0] = point1[0] + 1

    if point1[1] >= 5 and point2[1] == 1:
        point1[1] = point1[1] - 1
    elif point1[1] <= -5 and point2[1] == -1:
        point1[1] = point1[1] + 1

    return [point1 + point2 for point1, point2 in zip(point1, point2)]


def solution(dirs):
    move = {"U": [0, 1], "L": [-1, 0], "D": [0, -1], "R": [1, 0]}
    answer = 0

    point1 = [0, 0]

    box = []

    for i in dirs:
        tmp = str(point1[0]) + str(point1[1])
        point1 = cal(point1, move[i])
        try:
            tmp = tmp + i + str(point1[0]) + str(point1[1])
            box.append(tmp)
        except:
            tmp = tmp + i + str(point1[0]) + str(point1[1])
            box.append(tmp)

    print(box)
    result = list(set(box))
    print(result)
    answer = len(result)

    return answer


print(solution(input))
