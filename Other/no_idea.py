
def no_idea(array, A, B):
    happiness = 0
    for i in array:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1
    print(happiness)


no_idea([1, 5, 3], {1, 3}, {5, 7})