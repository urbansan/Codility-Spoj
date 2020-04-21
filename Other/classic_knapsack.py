def print_K(K):
    for line in K:
        print(line)
        # print()
    print()

def knapSack(W, wt, val, n):
    K = [[0]*(W+1) for _ in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(0, n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                # print(val[i - 1], K[i - 1][w - wt[i - 1]], w - wt[i - 1], K[i - 1][w])
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
            print_K(K)
    return K[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))