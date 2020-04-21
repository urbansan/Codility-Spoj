A = [
    [5, 3, 4],
    [1, 5, 8],
    [6, 4, 2]
]
#
A2 = [
    [4, 8, 2],
    [4, 5, 7],
    [6, 1, 6]
]




A3 = [
    [4, 8, 2],
    [4, 7, 7],
    [6, 1, 6]
]



A4 = [
    [2, 5, 4],
    [4, 6, 9],
    [4, 5, 2],
]

A5 = [
[9, 3, 3],
[3, 3, 2],
[1, 8, 1]
]
sq = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]





def cmp_lines(A, B):
    return sum([abs(a-b) for a, b in zip(A, B)])

def print_magic_square(s):
    print(*s[0], sep=' | ')
    print(*s[1], sep=' | ')
    print(*s[2], sep=' | ')

def rotate():
    S = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    RS = [
        [8, 3, 4],
        [1, 5, 9],
        [6, 7, 2]
    ]
    for s in S, RS:
        for _ in range(4):
            s[0][0], s[1][0], s[2][0], s[2][1], s[2][2], s[1][2], s[0][2], s[0][1] = \
                s[0][2], s[0][1], s[0][0], s[1][0], s[2][0], s[2][1], s[2][2], s[1][2],
            yield s

def minimalize(A):
    costs = []
    for s in rotate():
        cost = 0
        for baseline, line in zip(s, A):
            v = cmp_lines(baseline, line)
            cost += v
        # print_magic_square(s)
        # print(cost)
        costs.append(cost)
    return min(costs)




A = A5
a = minimalize(A)
print(a)


#
#
# for s in rotate():
#     print_magic_square(s)
#     print('-'*10)