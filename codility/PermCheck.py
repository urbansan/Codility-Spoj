def solution_sums(A):
    n = len(A)
    ref_sum = (n + 1) * n / 2
    real_sum = sum(A)
    uniq = set(A)
    if real_sum == ref_sum and n == len(uniq):
        return 1
    return 0

from collections import Counter
def solution_counter(A):
    A.sort()
    if len(A) != A[-1]:
        return 0
    elif len(set(Counter(A).values())) == 1:
        return 1
    return 0

