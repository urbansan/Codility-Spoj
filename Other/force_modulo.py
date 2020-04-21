import sys
from itertools import product


def F(args, M):
    s = sum([i * i for i in args])
    print(s)
    return s % M

def max_f(t):
    lines = [list(map(int, line.split())) for line in t.split('\n')]

    M = lines[0][1]
    # sum_ = sum(max_line(line, mod_val) for line in lines[1:])
    # for line in lines
    L = [set(line[1:]) for line in lines[1:]]
    A = set(product(*L))


    f_results = {args: F(args, M) for args in A}
    for args, res in f_results.items():
        if res == 766:
            print(args)
    return max(f_results.values())


T0 = '''3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 '''

T1 = '''6 767
2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304'''  # res = 763

print(max_f(T1))

# t = (488512261, 2, 1, 337650738, 2, 518538304)
# print(F(t, 767))