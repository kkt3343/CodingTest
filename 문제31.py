begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
#words = ["hot", "dot", "dog", "lot", "log"]

def differ_one_words(origin, target):
    length = len(origin)
    difference_intensity = 0
    for i in range(length):
        if origin[i] != target[i]:
            difference_intensity += 1
    if difference_intensity == 1:
        return "possible"
    else:
        return "impossible"

def solution(begin, target, words):
    answer = 9999
    # words안에 target이 없으면 return 0 하고 끝냅니다.
    key = False
    for i in words:
        if i == target:
            key = True
            break
    if key == False:
        print("단어가 없습니다.")
        return 0
    # 그 외에는 target으로 가는 경로를 찾는다.
    # DFS
    arr = []
    arr.append(begin)
    before_word = ""
    while len(arr) != 0:
        for i in range(len(arr)):
            before_word = arr.pop()
            for j in range(len(words)):
                if differ_one_words(before_word, words[j]) == "possible" and before_word != words[j]:
                    print(words[j])
                    arr.append(words[j])

    print(arr)

    return answer

ans = solution(begin, target, words)
#print(ans)

#print(differ_one_words("hot", words[1]))

# arr = []
# arr.append(begin)
# c = arr.pop()
# print(c)