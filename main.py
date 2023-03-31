# 백준 2636 치즈
import copy
import sys

inputString = """13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0"""

# a = []
# while True:
#     b = sys.stdin.readline().strip()
#     if not b:
#         break
#     a.append(b)
#
# inputString = ""
# for i in range(len(a)):
#     inputString = inputString + str(a[i]) + "\n"


# 파이썬 값 받는 작업 처리
sero = inputString.split(" ")[0]
garo = inputString.split(" ")[1].split("\n")[0]
box = []

for i in range(1, int(sero) + 1, 1):
    tmp = inputString.split("\n")[i]
    tmp2 = []
    for j in range(len(tmp)):
        if tmp[j] != ' ':
            tmp2.append(tmp[j])
    box.append(tmp2)

record = []
before_box = []
bbefore_box = []
record.append([0, 0])
outside = '@'


def melt_cheese():
    while len(record) != 0:
        tmp = record.pop()
        # 가로
        w = tmp[0]
        # 세로
        h = tmp[1]

        # 바깥쪽 공기는 모두 @ 로 채우자
        if box[w][h] == '0':
            box[w][h] = outside

        # 현재위치에서 좌측 검사
        if h != 0:
            if box[w][h - 1] == '0':
                record.append([w, h - 1])

        # 현재위치에서 우측 검사
        if h != int(garo) - 1:
            if box[w][h + 1] == '0':
                record.append([w, h + 1])

        # 현재위치에서 위쪽 검사
        if w != 0:
            if box[w - 1][h] == '0':
                record.append([w - 1, h])

        # 현재위치에서 아래쪽 검사
        if w != int(sero) - 1:
            if box[w + 1][h] == '0':
                record.append([w + 1, h])


def melting_cheese():
    for i in range(1, len(box) - 1, 1):
        for j in range(1, len(box[i]) - 1, 1):
            if box[i][j] == "1":
                if box[i][j - 1] == "@" or box[i][j + 1] == "@" or box[i - 1][j] == "@" or box[i + 1][j] == "@":
                    box[i][j] = "-1"

    for i in range(1, len(box) - 1, 1):
        for j in range(1, len(box[i]) - 1, 1):
            if box[i][j] == "-1":
                box[i][j] = "0"


def find_outside():
    for i in range(1, len(box) - 1, 1):
        for j in range(1, len(box[i]) - 1, 1):
            if box[i][j] == "@":
                if box[i][j - 1] == '0':
                    record.append([i, j - 1])
                elif box[i][j + 1] == '0':
                    record.append([i, j + 1])
                elif box[i - 1][j] == '0':
                    record.append([i - 1, j])
                elif box[i + 1][j] == '0':
                    record.append([i + 1, j])
                melt_cheese()


def print_cheese():
    for i in range(len(box)):
        for j in range(len(box[i])):
            print('%2s' % box[i][j], end=' ')
        print()
    global before_box
    global bbefore_box
    bbefore_box = copy.deepcopy(before_box)
    before_box = copy.deepcopy(box)


#
hours = 0
while True:
    if hours == 0:
        # 바깥 안쪽 체크 해야 합니다.
        melt_cheese()
    print(str(hours) + "번 째")
    print_cheese()
    melting_cheese()
    find_outside()
    if before_box == box:
        break
    hours += 1

# 이전 시간 치즈 모두 찾아 내기
cheese_count = 0
for i in range(len(bbefore_box)):
    for j in range(len(bbefore_box[i])):
        if bbefore_box[i][j] == "1":
            cheese_count += 1

print(str(hours))
print(str(cheese_count))

# print("걸린시간:" + str(hours))
# print("치즈개수:" + str(cheese_count))

