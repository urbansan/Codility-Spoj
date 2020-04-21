def bubble_sort(L: list):
    swaps_performed = True
    idx = max(len(L)-1, 0)
    while swaps_performed:
        swaps_performed = False
        for i in range(idx):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swaps_performed = True
        idx -= 1
    return L

new = bubble_sort([9, 1, 8, 3, 7, 4, 6])
print(new)

