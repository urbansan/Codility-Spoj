import statistics


def quicksort(A):
    j = len(A) - 1
    if j <= 0:
        return A

    i = 0
    med = statistics.median(A)
    while i < j:
        changed = False
        if A[i] < med:
            i += 1
            changed = True
        if A[j] > med:
            j -= 1
            changed = True

        if not changed:
            A[i], A[j] = A[j], A[i]
            i += 1
            if i != j-1:
                j -= 1

    left, right = quicksort(A[:i]), quicksort(A[i:])
    return left + right

print(quicksort([1, 3, 2, 5]))
print(quicksort([3, 3, 6, 5, 5, 3]))
print(quicksort([3, 3, 5, 1, 7, 6, 5, 3]))
print(quicksort([6, 5, 8, 3, 5, 7, 8, 3, 5, 6, 8, 9, 1, 4, 5, 6, 7, 8]))
print(quicksort(list(range(20, 0, -1))))
print(quicksort(list(range(20))))
print(quicksort([1, 2]*10))
print(quicksort([99]*10 + [1] + [10]*10))
