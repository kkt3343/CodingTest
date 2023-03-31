clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
#clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
def solution(clothes):
    answer = 0
    dictionary = {}
    for i in range(len(clothes)):
        try:
            dictionary[clothes[i][1]] += 1
        except:
            dictionary[clothes[i][1]] = 1

    tmp = 1
    for value in dictionary.values():
        tmp = tmp * (value+1)

    answer = tmp - 1
    return answer

#print(len(clothes))

c = solution(clothes)
print(c)