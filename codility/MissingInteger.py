def solution(A):
    A.sort()
    last_int = 0
    for el in filter(lambda x: x > 0, A):
        if el - 1 == last_int:
            last_int = el
    return last_int + 1