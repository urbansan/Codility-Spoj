RS = [
    [8, 3, 4],
    [1, 5, 9],
    [10, 7, 2]
]
sum_diag_a = 0
sum_diag_b = 0
for idx, row in enumerate(RS):
    sum_diag_a += row[idx]
    sum_diag_b += row[len(row) - idx - 1]

print(abs(sum_diag_a - sum_diag_b))