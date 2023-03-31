s = "banana"
#s = "aaabbaccccabba"
#s = "abracadabra"

def solution(s):
    answer = 0
    firstr = ""
    firstrCount = 0
    nonestrCount = 0
    #tmp = ""

    for i in s:
        if firstr == "":
            firstr = i
            firstrCount = firstrCount + 1
            #tmp = tmp + i
            answer = answer + 1

        elif firstr != i:
            nonestrCount = nonestrCount + 1
            #tmp = tmp + i
        else:
            firstrCount = firstrCount + 1
            #tmp = tmp + i

        if firstrCount == nonestrCount:
            #print(tmp)
            #tmp = ""
            firstr = ""

    return answer

print(solution(s))