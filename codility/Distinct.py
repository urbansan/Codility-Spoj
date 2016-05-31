import random

def solution(A):
	if A:
		A.sort()
		result = 1
		for k in xrange(1, len(A)):
			if A[k] != A[k - 1]:
				result += 1
		return result
	else:
		return 0



A = [random.randint(-10, 10) for i in range(100)]

print solution(A)
print A