a = "f2{a3{bc}}z"

def solution(a):
    ans = ''
    arr = []
    i = 0
    while i < len(a):
        arr.append(a[i])
        print(arr)

        tmp = []
        repeat = 0
        while True:
            if arr[len(arr)-1].isdigit():
                break
            if arr[len(arr)-1] == "{":
                break
            if arr[len(arr)-1] == "}":
                while True:
                    c = arr.pop()
                    if c == "{":
                        repeat = int(arr.pop())
                        break
                    else:
                        tmp.append(c)
            else:
                break
            if len(arr) == 0:
                break
        i += 1
        print(tmp)
        # str = re.match('[a-z]', a[i])
        # num = re.match('[0-9]', a[i])
        #
        #
        # if str is not None:
        #     arr.append(str.group(0))
        # if num is not None:
        #     arr.append(num.group(0))
        # i += 1

            #print(num.group(0))

solution(a)


# k = ['a','b', "5"]
# print(k[2].isdigit())
# print(k)