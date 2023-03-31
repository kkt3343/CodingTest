progresses = [93, 30, 55]
speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

def cal(point1, point2):
    return [point1 + point2 for point1, point2 in zip(point1, point2)]

def solution(progresses, speeds):
    answer = []

    successIndex = 0
    while True:
        #작업종료
        successCount = 0
        for i in progresses:
            if i >= 100:
                successCount = successCount + 1
        if successCount == len(progresses):
            break

        progresses = cal(progresses, speeds)
        z = 0
        for i in range(successIndex, len(progresses), 1):
            if progresses[i] < 100:
                break
            z = z + 1
            successIndex = successIndex + 1
        #print(z)
        if z > 0:
            answer.append(z)
    return answer

c = solution(progresses, speeds)
print(c)