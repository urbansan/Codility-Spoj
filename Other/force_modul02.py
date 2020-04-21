import itertools


# (K, N) = map(int, raw_input().split())
#
# L = list()
# for i in range(K):
#     l = map(int, raw_input().split())
#     n = l[0]
#     L.append(l[1:])
#     assert len(L[i]) == n
def mx_t(t):
    lines = [list(map(int, line.split())) for line in t.split('\n')]

    m = lines[0][1]
    l = [set(line) for line in lines [1:]]
    n = lines[0][0]

    # from itertools import product
    # n, m = [int(x) for x in input().split()]
    l1 = list()
    for i in range(n):
        l = list(map(int, l))[1:]
        l1.append(l)
    r = map(lambda x: sum(i * i for i in x) % m, product(*l1))
    print(max(r))

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


mx_t(T1)

from itertools import product
n,m=[int (x) for x in input().split()]
l1=list()
for i in range(n):
    l=list(map(int,input().split()))[1:]
    l1.append(l)
r=map(lambda x:sum(i*i for i in x)%m,product(*l1))
print(max(r))