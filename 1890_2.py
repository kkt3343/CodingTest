# size = int(input())
# box=[]
#
# for i in range(size):
#     box.append(list(map(int,input().split())))
#
# route_arr=[[0]*size for i in range(size)]
#
# route_arr[size-1][size-1] = 1

inputString = """9
3 1 2 2 3 3 1 1 2
1 1 2 1 1 2 3 1 2
2 1 1 3 2 2 1 3 1
3 3 1 1 1 3 1 2 1
3 2 2 2 1 1 3 3 1
3 1 3 2 2 3 1 3 3
3 1 1 2 1 1 1 1 1
2 3 1 3 1 3 2 2 2
3 3 3 2 3 1 3 3 0
"""


# inputString = """4
# 2 3 3 1
# 1 2 1 3
# 1 2 3 1
# 3 1 1 0"""

# 파이썬 값 받는 작업 처리
size = int(inputString.split("\n")[0])

box = []
for i in range(1, int(size) + 1, 1):
    tmp = inputString.split("\n")[i]
    tmp2 = []
    for j in range(len(tmp)):
        if tmp[j] != ' ':
            tmp2.append(int(tmp[j]))
    box.append(tmp2)

route_arr=[[0]*size for i in range(size)]


def isValid(x, y):
    # 오른쪽 하단만 갈 수 있어서 0 체크는 할 필요는 없다.
    if x > int(size) - 1 or y > int(size) - 1:
        return False
    else:
        return True

route_arr[size-1][size-1] = 1

for n in range(size - 1, -1, -1):
    # 가로
    for i in range(n, -1, -1):
        if n == size -1 and i == n:
            continue
        move_number = box[n][i]
        down = 0
        right = 0
        if isValid(n + move_number, i):
            down = route_arr[n + move_number][i]
        if isValid(n, i + move_number):
            right = route_arr[n][i + move_number]

        route_arr[n][i] = down + right

    # 세로
    for i in range(n, -1, -1):
        if n == size -1 and i == n:
            continue
        move_number = box[i][n]
        down = 0
        right = 0
        if isValid(i + move_number, n):
            down = route_arr[i + move_number][n]
        if isValid(i, n + move_number):
            right = route_arr[i][n + move_number]
        route_arr[i][n] = down + right

print(route_arr[0][0])



