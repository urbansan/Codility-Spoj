from collections import Counter

def solution(A):
    return filter(lambda x: x[1] % 2 != 0, Counter(A).items())[0][0] # stupid python 2.7 structure


A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))

