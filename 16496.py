# 큰 수 만들기
import sys
input = sys.stdin.readline

N = int(input())
tmp = input()
arr = tmp.split("\n")[0]
arr = arr.split(" ")

from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(lambda x,y: int(x+y)-int(y+x)), reverse=True)
    return ''.join(numbers)

key = False
for i in range(len(arr)):
    if arr[i] != "0":
        key = True
        break
if not key:
    print(0)
else:
    print(solution(arr))