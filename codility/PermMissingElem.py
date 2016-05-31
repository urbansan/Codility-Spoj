
from random import shuffle


def solution(ar):
	if not ar:
		return 1
	ar.sort()
	if ar[0] != 1:
		return 1
	for i in range(1, len(ar)):
		if (ar[i] - 1) != ar[i-1]:
			return ar[i] - 1

	return len(ar) + 1




# A = [3, 1, 2, 4, 3, 10, 3, 6, 4, 6, 8, 9, 78, 5, 3, 2, 0, -3, -4, -6, -14, -200, -10, 100]
# A = [-1000, 1000]
# A = [2, 3, 1, 4]
# A = [3, 2]
A = []
# A = [3]


print solution(A)

