

def solution(A):
    A.sort()
    if not A or A[0] != 1:
        return 1
    
    for en, el in enumerate(A):
        if en + 1 != el:
            return en + 1
    return el + 1


A = [3, 2]
print(solution(A))

A = [2, 3, 1, 4]
print(solution(A))

A = [2, 3, 1, 5]
print(solution(A))

A = [2, 3, 1, 5, 8, 7, 6]
print(solution(A))

# A = [2, 3, 1, 5]
# print(solution(A))
#
# A = [2, 3, 1, 5]
# print(solution(A))
