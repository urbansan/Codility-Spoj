from functools import reduce
def solution(A):
    if A and len(A) > 1:
        A.sort(key=lambda x: abs(x))
        sums_left = [0] * (len(A) + 1)
        sums_right = [0] * (len(A) + 1)

        for i, el in enumerate(A, start=1):
            sums_left[i] = sums_left[i-1] + abs(el)
            sums_right[-(i+1)] = sums_right[-i] + abs(A[-(i)])
        diff_list = list(map(lambda x, y: abs(x - y), sums_left[1:-1], sums_right[1:-1]))
        min1 = min(diff_list)

        Ac = list(A)
        Ac.sort(key=lambda x: abs(x), reverse=True)
        Ac[0] = abs(Ac[0])
        min3 = reduce(lambda x, y: abs(x - abs(y)), Ac)
        return min(min1, min3)
    elif len(A) == 1:
        return abs(A[0])
    else:
        return 0