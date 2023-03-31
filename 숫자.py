a = [5, 5, 9, 9, 9]
b = [3, 4, 4, 4, 4, 1]

def solution(a, b):
    length = 0
    short_length = 0
    if len(a) >= len(b):
        length = len(a)
        short_length = len(b)
    else:
        length = len(b)
        short_length = len(a)
        c = []
        c = a
        a = b
        b = c

    over = 0
    ans = []
    for i in range(-1, -1 * length - 1, -1):
        if i > -1 * short_length - 1:
            tmp = a[i] + b[i] + over
            ans.append(tmp % 10)
            over = int(tmp / 10)
        else:
            tmp = a[i] + over
            ans.append(tmp % 10)
            over = int(tmp / 10)

    if over == 1:
        ans.append(over)

    ans.reverse()
    #print(ans)
    return ans


p = solution(a, b)
print(p)