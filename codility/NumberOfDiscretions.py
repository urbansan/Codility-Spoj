import random
from itertools import combinations, permutations, product

def solution1(ar):
	sumator = 0
	n = len(ar)
	ar_count = [[] for i in xrange(n)]
	for i in xrange(n):
		left = i - ar[i] if i - ar[i] >= 0 else 0
		right = i + ar[i] if i + ar[i] < n else n - 1
		for j in xrange(left, right + 1):
			ar_count[j].append(i)

	listForSet = []
	for i in xrange(n):
		left = i - ar[i] if i - ar[i] >= 0 else 0
		right = i + ar[i] if i + ar[i] < n else n - 1
		for j in xrange(left, right + 1):
			listForSet += listForSet + ar_count[j]

		listForSet = list(set(listForSet))
		listForSet.remove(i)

		sumator += len(listForSet)
		if sumator > 2e7:
			return -1
		
		del listForSet
		listForSet = []
	print ar
	print ar_count
	return int(sumator / 2.)

def solution(ar):
	sumator = 0
	n = len(ar)
	ar_count = [[] for i in xrange(n)]
	listForSet = []
	for i in xrange(n):
		left = i - ar[i] if i - ar[i] >= 0 else 0
		right = i + ar[i] if i + ar[i] < n else n - 1
		for j in xrange(left, i + 1):
			# zliczam siebie i usuwam
			# ar_count[j].remove(i)
			listForSet += listForSet + ar_count[j]

		listForSet = list(set(listForSet))
		print listForSet

		sumator += len(listForSet)
		if sumator > 2e7:
			return -1
		
		listForSet = []

		for j in xrange(i, right + 1):
			# dodaje siebie
			ar_count[j].append(i)

	print ar_count
	return sumator



A = [random.randint(-10, 10) for i in range(100)]
A = [1,5,2,1,4,0]

print A
print solution(A)