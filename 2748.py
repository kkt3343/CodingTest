index = int(input())

fibo = [0, 1]
if index == 0:
    print(fibo[0])
elif index == 1:
    print(fibo[1])
else:
    for i in range(2, index + 1):
        bbefore = fibo[i - 2]
        before = fibo[i - 1]
        fibo.append(bbefore + before)
    print(fibo[index])
