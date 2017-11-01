def solution(A):
    full_sum = sum(A)
    cur_sum = A[0]
    min_diff = abs(A[0] - (full_sum - A[0]))
    for el in A[1:-1]:
        cur_sum += el
        min_diff = min(min_diff, abs(cur_sum - (full_sum - cur_sum)))
    return min_diff


A = [3, 1, 2, 4, 3]
print(solution(A))
A = [3, 1, 2, -4, 3]
print(solution(A))

A = [-1000, 1000]
print(solution(A))

A = [1000, -1000]
print(solution(A))

A = [1000, 1000]
print(solution(A))

A = [-1000, -1000, -1000]
print(solution(A))

A = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
print(solution(A))