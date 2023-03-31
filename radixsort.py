numbers = [3, 30, 34, 5, 9, 33, 369, 367]

from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
    return ''.join(numbers)

#lambda x, y: int(x+y)-int(y+x)), reverse=True

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y == y + x:
        return 0
    else:
        return 1

print(solution(numbers))