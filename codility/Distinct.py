import random

def solution(A):
	return len(set(A))



A = [random.randint(-10, 10) for i in range(100)]

print solution(A)
print A