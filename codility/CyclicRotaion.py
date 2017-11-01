

def solution(A, K):
    if A:
        slice_idx = len(A) - K % len(A)
        return A[slice_idx:] + A[:slice_idx]
    return A

A = [3, 8, 9, 7, 6]
print([9, 7, 6, 3, 8] == solution(A, 3))

A = [3, 8, 9, 7, 6]
print([6, 3, 8, 9, 7] == solution(A, 6))

solution([], 6)