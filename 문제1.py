numberp = [2,1,3,4,1]
#numberp = [5,0,2,7]

def solution(numbers):
    answer = []
    for i in range(0, len(numbers), 1):
        for j in range(i+1, len(numbers), 1):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer

c = solution(numberp)
print(c)
print(type(c[0]))

# def solution2(numbers):
#     answer = []
#     for i in range(0, len(numbers), 1):
#         for j in range(i+1, len(numbers), 1):
#             print(numbers[i], numbers[j], end=",")
#     print()
#     return answer
#
# solution2(numberp)