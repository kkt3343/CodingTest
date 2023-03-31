#p = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
#p = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
p = ["hello", "one", "even", "never", "now", "world", "draw"]
#p = ['ac','ca','ac','ac']

def solution(n, words):
    answer = []
    tmpdict = {}
    key = False
    x = 1
    y = 1

    for i in range(len(words)):
        #우선 중복인지 검사먼저
        try:
            key = False
            tmpdict[words[i]] += 1
        except:
            key = True
            tmpdict[words[i]] = 1
        if key == False:
            answer.append(x)
            answer.append(y)
            return answer
        #중복이 아니라면 다음것이 연관이 없는지 확인
        if i != len(words) - 1:
            if words[i][(len(words[i]) - 1)] != words[i + 1][0]:
                if x == n:
                    x = x % n
                    y = y + 1
                x = x + 1
                answer.append(x)
                answer.append(y)
                return answer

        if x == n:
            x = x % n
            y = y + 1
        x = x + 1

    answer.append(0)
    answer.append(0)
    return answer

print(solution(2, p))

