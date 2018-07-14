def genomic_range_query(Seq, L, R):
    n = len(Seq) + 1
    sums = [[0] * n, [0] * n, [0] * n, [0] * n]
    for i in range(1, n):
        if Seq[i-1] == 'A':
            sums[0][i] += 1
        elif Seq[i-1] == 'C':
            sums[1][i] += 1
        elif Seq[i-1] == 'G':
            sums[2][i] += 1
        else:
            sums[3][i] += 1

        if i < n - 1:
            sums[0][i+1] = sums[0][i]
            sums[1][i+1] = sums[1][i]
            sums[2][i+1] = sums[2][i]
            sums[3][i+1] = sums[3][i]

    r_box = []
    minis = 0
    slownik = {
        'A' : 1,
        'C' : 2,
        'G' : 3,
        'T' : 4
    }
    for i in range(len(L)):
        if L[i] == R[i]:
            minis = slownik[Seq[L[i]]]
        elif sums[0][L[i]] < sums[0][R[i]+1]:
            minis = 1
        elif sums[1][L[i]] < sums[1][R[i]+1]:
            minis = 2
        elif sums[2][L[i]] < sums[2][R[i]+1]:
            minis = 3
        else:
            minis = 4
        r_box.append(minis)

    return r_box
