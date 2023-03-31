# 구간 합 구하기
import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())

# 간단하게 처리하려면 x4만큼 사용함
tree = [0] * (N * 4)
arr = []
for i in range(N):
    arr.append(int(input()))


# 세그먼트 트리 만들기 start는 0 고정 end는 입력의 길이, 첫 인덱스는 항상 1
def init(start, end, index):
    # 가장 끝에 도달했으면 arr 삽입 (즉 쪼개지지 않는 상황임)
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채워준다.
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

# left , right 값만 잘 설정하면 된다.
def tree_sum(start, end, index, left, right):
    # 이 것은 내가 2 ~ 6을 알고 싶은데 해당 구간은 0 ~ 1의 값을 저장하고 있으면 이 구간은 필요 없다.
    if left > end or right < start:
        return 0

    # 2 ~ 6을 값을 알고 싶은데 3 ~ 4의 값을 저장하고 있다면 이 값은 가져오게 된다.
    if left <= start and right >= end:
        #print(tree[index] , end=' ')
        return tree[index]

    # 예를 들어 해당 노드가 0 ~ 4 의 값을 가지고 있는데 내가 2 ~ 6번 째 값을 알고 싶으면
    # start = 0 end = 4 left = 2 right = 6
    # 즉 나눠야 한다. 나누는 것은 항상 길이의 절반을 쪼개서 구간합을 구한다.
    mid = (start + end) // 2
    return tree_sum(start, mid, index * 2, left, right) + tree_sum(mid + 1, end, index * 2 + 1, left, right)

# 값 수정하기
# start, end, index는 고정 what은 어떤 위치의 값을 어떻게 변하게 할지 정한다.
def update(start, end, index, what, value):
    #what이 3이라면 arr의 4번째 값을 바꾸는 것이다.
    if start > what or end < what:
        return
    #범위에 속하면 이 값은 갱신해야 한다.
    tree[index] += value
    #리프노드면 끝내기
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


# 세그먼트 트리 제작
init(0, len(arr) - 1, 1)
#print(tree)

# 결론 주문대로 작업부분이 잘못 되었다.
for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        temp = c - arr[b-1]
        arr[b-1] = c
        update(1, N, 1, b, temp)

    elif a == 2:
        print(tree_sum(1, N, 1, b, c))

    #print(tree)

# # 주문대로 작업한다.
# for i in range(M+K):
#     a, b, c = map(int, input().split())
#     # update
#     if a == 1:
#         update(1, len(arr) - 1, 1, b - 1, (c - arr[b - 1]))
#         arr[b - 1] = c
#     # 합계 구하기
#     elif a == 2:
#         #print(tree_sum(0, len(arr) - 1, 1, b - 1, c))
#         print(tree_sum(1, len(arr), 1, b, c))
#     print(tree)

# 8 2 2
# 10
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 5
#
#
# 맞음
# [0, 45, 19, 26, 12, 7, 11, 15, 10, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# [0, 45, 19, 26, 12, 7, 11, 15, 10, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 48, 22, 26, 12, 10, 11, 15, 10, 2, 6, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 2 10 5 17
# [0, 48, 22, 26, 12, 10, 11, 15, 10, 2, 6, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 45, 22, 23, 12, 10, 8, 15, 10, 2, 6, 4, 2, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# 10 2 12
# [0, 45, 22, 23, 12, 10, 8, 15, 10, 2, 6, 4, 2, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# 틀림
# [0, 45, 19, 26, 12, 7, 11, 15, 10, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# [0, 45, 19, 26, 12, 7, 11, 15, 10, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 48, 22, 26, 15, 7, 11, 15, 10, 5, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 5 7 5 17
# [0, 48, 22, 26, 15, 7, 11, 15, 10, 5, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 45, 19, 26, 15, 4, 11, 15, 10, 5, 3, 1, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# 4 5 9
# [0, 45, 19, 26, 15, 4, 11, 15, 10, 5, 3, 1, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]