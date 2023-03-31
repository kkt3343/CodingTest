def ppp(titles, p):
    tmp = p[0]

    box = []
    for i in range(len(tmp)):
        c = tmp[i].split(' ')
        inner = []
        for j in range(len(c) - 1):
            inner.append(titles[int(c[j])])
        box.append(inner)
    return box

def solution(titles, lyrics, problems):
    dic = dict.fromkeys(problems, "")
    #print(dic)
    idx = []

    for i, k in dic.items():
        for l, j in enumerate(lyrics):
            if j.startswith(i):
                dic[i] += str(l) + str(" ")
    #print(dic)

    idx = [list(dic.values())]
    #print(idx)

    return ppp(titles, idx)


ans = solution(["아모르파티", "아기상어", "올챙이와개구리", "산다는건", "A", "B", "C", "D", "E", "F", "G"],
         ["산다는게다그런거지누구나빈손으로와", "아기상어뚜루루뚜루귀여운뚜루루뚜루", "개울가에올챙이한마리꼬물꼬물헤엄치다", "산다는건다그런거래요힘들고아픈날도많지만", "A", "B", "C", "D", "E", "F", "G"],
         ["산다", "아기상어", "올챙이", "산다는", "G"]
         )

print(ans)