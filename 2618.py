inputString = """6
3
3 5
5 5
2 3"""

size = int(inputString.split("\n")[0])
accident_count = int(inputString.split("\n")[1].split("\n")[0])

accident = []
for i in range(2, accident_count + 2):
    accident.append([int(inputString.split("\n")[i].split(' ')[0]), int(inputString.split("\n")[i].split(' ')[1])])

print(size, accident_count, accident)


# 항상 경찰차 1은 1,1 에 존재하고
# 항상 경찰차 2는 n,n 에 존재한다.

# 거리 구하기 공식
def calculate_distance(policecar_x, policecar_y, accident_x, accident_y):
    return abs(accident_x - policecar_x) + abs(accident_y - policecar_y)


print(calculate_distance(1, 1, accident[0][0], accident[0][1]))
