size = int(input())
box=[]

for i in range(size):
    box.append(list(map(int,input().split())))

route_arr=[[0]*size for i in range(size)]

# 기본 설정
box[int(size)-1][int(size)-1] = "T"


def isValid(x, y):
    # 오른쪽 하단만 갈 수 있어서 0 체크는 할 필요는 없다.
    # 테이블 바깥 으로 나가지 못하게 설정
    if x > int(size) - 1 or y > int(size) - 1:
        return False
    else:
        return True

def isValid_route(xx, yy):
    if route_arr[xx][yy] == 0:
        return True
    else:
        return False



position = []
position.append([0, 0])

while len(position) != 0:
    tmparr = position[len(position)-1]
    x = tmparr[0]
    y = tmparr[1]
    move_number = box[x][y]

    c = route_arr[x][y]

    if move_number == 0:
        position.pop()
        route_arr[x][y] = "F"
        continue

    if move_number == "T":
        position.pop()
        tmparr2 = position.pop()
        route_arr[tmparr2[0]][tmparr2[1]] = 1
        continue

    vaild_count = 0
    if not isValid(x, y + move_number):
        vaild_count += 1
    if not isValid(x + move_number, y):
        vaild_count += 1
    if vaild_count == 2:
        route_arr[x][y] = "F"
        position.pop()
        continue

    right = 0
    down = 0
    old_number = route_arr[x][y]
    if isValid(x, y + move_number):
        if not route_arr[x][y + move_number] == "F":
            right = route_arr[x][y + move_number]

    if isValid(x + move_number, y):
        if not route_arr[x + move_number][y] == "F":
            down = route_arr[x + move_number][y]

    if not isValid(x, y + move_number):
        if isValid(x + move_number, y):
            if route_arr[x + move_number][y] == "F":
                route_arr[x][y] = "F"
                position.pop()
                continue

    if not isValid(x + move_number, y):
        if isValid(x, y + move_number):
            if route_arr[x][y + move_number] == "F":
                route_arr[x][y] = "F"
                position.pop()
                continue

    if old_number == right + down:
        key1 = False
        key2 = False
        if isValid(x, y + move_number):
            if route_arr[x][y + move_number] != 0:
                key1 = True
        else:
            key1 = True
        if isValid(x + move_number, y):
            if route_arr[x + move_number][y] != 0:
                key2 = True
        else:
            key2 = True

        if key1 and key2:
            position.pop()

    else:
        route_arr[x][y] = right + down


    if isValid(x, y + move_number):
        if route_arr[x][y + move_number] == 0:
            position.append([x, y + move_number])

    if isValid(x + move_number, y):
        if route_arr[x + move_number][y] == 0:
            position.append([x + move_number, y])


print(route_arr[0][0])