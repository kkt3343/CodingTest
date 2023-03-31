def solution(titles, lyrics, problems):
    dic = dict.fromkeys(problems, "")
    idx = []

    for i, k in dic.items():
        for l, j in enumerate(lyrics):
            if j.startswith(i):
                dic[i] += str(l)

    idx = [list(dic.values())]

    # lst=[]
    # for i in idx[0]:
    #     print(list(map(int,i)))
    #     for k in list(map(int,i)):
    #         print(k)
    #         print(titles[k])
    #         lst.append(titles[k])
    # print(lst)

    lst = [list(map(int, i)) for i in idx[0]]

    # print(titles)
    # print(lst)

    k = 0
    for i in lst:
        # print(i)
        for j in range(len(i)):
            # print(titles[i[j]], end=' ')
            lst[k][j] = titles[i[j]]
        # print()
        k = k + 1

    # print(titles)
    testarr = []
    for i in range(len(titles)):
        testarr.append((titles[i], i))

    print(testarr)

    aaa = []
    for i in range(len(lst)):
        aaa.append(sorted(lst[i], key=lambda x: x[1], reverse=True))

    #print(aaa)
    return aaa
    # return lst
    # print(lst)


ans = solution(["아모르파티", "아기상어", "올챙이와개구리", "산다는건"],
               ["산다는게다그런거지누구나빈손으로와", "아기상어뚜루루뚜루귀여운뚜루루뚜루", "개울가에올챙이한마리꼬물꼬물헤엄치다", "산다는건다그런거래요힘들고아픈날도많지만"],
               ["산다", "아기상어", "올챙이"]
               )
print(ans)
