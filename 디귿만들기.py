global p

def makeDi(origin_arr, present, depth):
    if present == depth:
        global p
        p = origin_arr
        #print(origin_arr)
        return
    new_arr = [[0 for j in range(pow(2, present))] for i in range(pow(2, present))]
    if present == 1:
        new_arr[0][0] = 2
        new_arr[0][1] = 1
        new_arr[1][0] = 3
        new_arr[1][1] = 4
    else:
        # 이전 값 채워넣기 (1사분면)
        for i in range(0, pow(2, present - 1), 1):
            for j in range(-1, -1 * pow(2, present - 1) - 1, -1):
                new_arr[i][j] = origin_arr[i][j]

        x = 0
        # 2사분면
        for i in range(0, pow(2, present - 1), 1):
            y = 0
            for j in range(-1 * pow(2, present - 1) - 1, -1 * pow(2, present) - 1, -1):
                y = y - 1
                new_arr[i][j] = origin_arr[x][y] + (pow(2, present)) * (pow(2, present - 2))
            x = x + 1

        x = 0
        # 3사분면
        for i in range(pow(2, present - 1), pow(2, present), 1):
            y = 0
            for j in range(-1 * pow(2, present - 1) - 1, -1 * pow(2, present) - 1, -1):
                y = y - 1
                new_arr[i][j] = origin_arr[x][y] + ((pow(2, present)) * 2) * (pow(2, present - 2))
            x = x + 1

        x = 0
        # 4사분면
        for i in range(pow(2, present - 1), pow(2, present), 1):
            y = 0
            for j in range(-1, -1 * pow(2, present - 1) - 1, -1):
                y = y - 1
                new_arr[i][j] = origin_arr[x][y] + ((pow(2, present)) * 3) * (pow(2, present - 2))
            x = x + 1

    makeDi(new_arr, present + 1, depth)


def solution(n, i, j):
    depth = 0

    while n > 1:
        n = n / 2
        depth += 1

    base = [1]
    makeDi(base, 1, depth + 1)

n = 16
solution(n, 2, 3)
for i in range(n):
    for j in range(n):
        print("%4d"%p[i][j], end=" ")
    print()

