import sys
input = sys.stdin.readline

N, K = map(int,input().split())

tmp = N // 2
if tmp < K:
    K = N - K
print(N, K)