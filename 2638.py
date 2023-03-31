# 백준 2638 치즈
import copy
import sys

# 세로 가로
inputString = """8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0"""

# 백준 전용 인풋 코드 (타 사용시 배제 해야함)
a = []
while True:
    b = sys.stdin.readline().strip()
    if not b:
        break
    a.append(b)

inputString = ""
for i in range(len(a)):
    inputString = inputString + str(a[i]) + "\n"

#############################################

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
record.append([0, 0])




# 인덱스 벗어나지 않게 설정
def trueIndex(insero, ingaro):
    if insero < 0 or ingaro < 0 or insero >= int(sero) or ingaro >= int(garo):
        return False
    else:
        return True


# 치즈 출력용
def print_cheese():
    for i in range(len(box)):
        for j in range(len(box[i])):
            print('%2s' % box[i][j], end=' ')
        print()
    print()

def melt_cheese():
    while len(record) != 0:
        tmp = record.pop()
        # 세로
        h = tmp[0]
        # 가로
        w = tmp[1]

        # 바깥쪽 공기는 모두 A 로 채운다
        if trueIndex(h, w):
            if box[h][w] == "0":
                box[h][w] = 'A'

        # 현재 위치 에서 좌측 검사
        if trueIndex(h, w - 1):
            if box[h][w - 1] == '0':
                record.append([h, w - 1])

        # 현재 위치 에서 우측 검사
        if trueIndex(h, w + 1):
            if box[h][w + 1] == '0':
                record.append([h, w + 1])

        # 현재 위치 에서 위쪽 검사
        if trueIndex(h - 1, w):
            if box[h - 1][w] == '0':
                record.append([h - 1, w])

        # 현재 위치 에서 아래쪽 검사
        if trueIndex(h + 1, w):
            if box[h + 1][w] == '0':
                record.append([h + 1, w])


def melting_cheese():
    for i in range(1, len(box) - 1, 1):
        for j in range(1, len(box[i]) - 1, 1):
            cheese_count = 0
            if box[i][j] == "1":
                if box[i][j - 1] == "A":
                    cheese_count += 1
                if box[i][j + 1] == "A":
                    cheese_count += 1
                if box[i - 1][j] == "A":
                    cheese_count += 1
                if box[i + 1][j] == "A":
                    cheese_count += 1
                if cheese_count >= 2:
                    box[i][j] = "B"

def melted_cheese():
    for i in range(1, len(box) - 1, 1):
        for j in range(1, len(box[i]) - 1, 1):
            if box[i][j] == "B":
                box[i][j] = "0"


def find_outside():
    for i in range(1, len(box) - 1, 1):
        for j in range(1, len(box[i]) - 1, 1):
            if box[i][j] == "0":
                if box[i][j - 1] == 'A':
                    record.append([i, j - 1])
                elif box[i][j + 1] == 'A':
                    record.append([i, j + 1])
                elif box[i - 1][j] == 'A':
                    record.append([i - 1, j])
                elif box[i + 1][j] == 'A':
                    record.append([i + 1, j])
                melt_cheese()


p = 0
before = []
while True:
    key = True
    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] != 'A':
                key = False
    if key:
        break

    if p == 0:
        melt_cheese()
    else:
        before = copy.deepcopy(box)
        melting_cheese()
        melted_cheese()
        find_outside()
    p = p + 1

print(p-1)


# melt_cheese()
# print_cheese()
#
# melting_cheese()
# print_cheese()
# melted_cheese()
# print_cheese()
# find_outside()
# print_cheese()
#
# melting_cheese()
# print_cheese()
# melted_cheese()
# print_cheese()
# find_outside()
# print_cheese()
#
# melting_cheese()
# print_cheese()
# melted_cheese()
# print_cheese()
# find_outside()
# print_cheese()
#
# melting_cheese()
# print_cheese()
# melted_cheese()
# print_cheese()
# find_outside()
# print_cheese()

# while True:
#     key = True
#     for i in range(len(box)):
#         for j in range(len(box[i])):
#             if box[i][j] != 'A':
#                 key = False
#     if key:
#         break
#
#     before = copy.deepcopy(box)
#     if p == 0:
#         melt_cheese()
#     else:
#         find_outside()
#         melting_cheese()
#         find_outside()
#     p = p + 1
#
# count = 0
# for i in range(len(before)):
#     for j in range(len(before[i])):
#         if before[i][j] == '1':
#             count = count + 1
# print(p-1)
# print(count)


