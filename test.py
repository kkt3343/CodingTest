import sys

a = []
while True:
    b = sys.stdin.readline().strip()
    if not b:
        break
    a.append(b)

inputString = ""
for i in range(len(a)):
    inputString = inputString + str(a[i]) + "\n"

print(inputString)