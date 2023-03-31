words = ["hello", "hell", "good", "goose", "children", "card", "teachable"]
queries = ["hell*", "goo*", "*able", "qua*"]


# words = ["zero", "base", "students", "are", "the", "best"]
# queries = ["zewrwe*", "*e", "s*"]

def solution(words, queries):
    ans = []
    for i in range(len(queries)):
        ans.append(0)

    for j in range(len(words)):
        text = ""
        for i in range(len(queries)):
            # hell*
            left = queries[i].split("*")[0]
            # *able
            right = queries[i].split("*")[1]

            key = ""
            if left == "":
                text = right
                key = "right"
            else:
                text = left
                key = "left"

            pp = True
            if key == "right":
                try:
                    for k in range(-1, -1 * len(text) - 1, -1):
                        #print(words[j][k], text[k], end=", ")
                        if words[j][k] != text[k]:
                            pp = False
                            break
                except:
                    pp = False
            else:
                try:
                    for k in range(len(text)):
                        #print(words[j][k], text[k], end=", ")
                        if words[j][k] != text[k]:
                            pp = False
                            break
                except:
                    pp = False
            if pp:
                ans[i] += 1

        #print()
            #print(text, end=' : ')
            #print(text in words[j], end=' ')
        #print()
    return ans

print(solution(words, queries))
