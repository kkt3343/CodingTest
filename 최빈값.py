def solution(array):
    answer = 0
    bindo = 0
    dictionary = {}
    for i in range(len(array)):
        try:
            dictionary[array[i]] += 1
        except:
            dictionary[array[i]] = 1


    for key, value in dictionary.items():
        if bindo < value:
            bindo = value
            answer = key

    tmp = 0
    for value in dictionary.values():
        if value == bindo:
            tmp = tmp + 1
        if tmp == 2:
            return -1

    return answer

s = [1, 2, 3, 3, 3, 3, 3, 4]
#s = [1, 1, 2, 2]
# s = [1]
c = solution(s)
print(c)

# arr = [1, 2, 3, 3, 3, 4]
# dictionary = {}
#
# dictionary[arr[0]] = 5
#
# dictionary[arr[0]] = dictionary[arr[0]] + 1
#
# print(dictionary)

#for i in range(len(arr)):

