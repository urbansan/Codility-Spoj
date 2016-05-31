import random

def solution(ar):
	ar.sort()
	n = len(ar)
	posProd = ar[n-1] * ar[n-2] * ar[n-3]
	negProd = ar[0] * ar[1] * ar[n-1]

	if posProd > negProd:
		return posProd
	else:
		return negProd




A = [random.randint(-100, 100) for i in range(10)]
A = [-1] * 10
A = [-3, 1, 2, -2, 5, 6]
# print A
print solution(A)
print A