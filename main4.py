import math

def get_gcd(num1, num2):
    return get_gcd(num2, num1 % num2) if num1 % num2 else num2

def gradient_cal(w,h):
    answer = w * h
    temp = 0
    gradient = w / h
    for i in range(h):
        before = i * gradient
        next = (i + 1) * gradient

        if int(next) == next:
            temp = temp + 1
        elif math.floor(next) - math.floor(before) == 0:
            temp = temp + 1
        elif (math.floor(next) - math.floor(before) == 1):
            temp = temp + 2

    answer = answer - temp
    return answer

def solution(w,h):
    if w > h:
        tmps = w
        w = h
        h = tmps

    answer = 0
    #기약분수화 시키기
    g = get_gcd(w, h)
    new_w = w / g
    new_h = h / g

    #먼저 대각선과 연관 없는 부분 먼저 싹 구하기
    answer = answer + (w) * (h - new_h)

    #대각선에 영향받는 부분만 잘라서 계산
    tmp = gradient_cal(int(new_w), int(new_h))
    tmp = tmp * g

    answer = answer + tmp
    answer = int(answer)
    return answer

print(solution(12,8))
