Is there any way to simplify the code of Python below?

N = 10
branches = [6, 7, 10, 16, 12]

m = max(branches)

for i in range(m, 0, -1):
    count = 0
    key = False
    for j in range(len(branches)):
        count = count + (branches[j] // i)
        if count >= N:
            print(i)
            key = True
            break
    if key:
        break
