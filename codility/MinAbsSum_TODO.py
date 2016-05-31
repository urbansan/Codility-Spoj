import random
from itertools import combinations, permutations, product

def solution(ar):

	negSum = 0
	posSum = 0
	minSum = 0
	Sminsum = []
	S = []
	for i in range(len(ar)):
		negSum = abs(minSum - ar[i])
		posSum = abs(minSum + ar[i])
		if posSum < negSum:
			S.append(1)
			minSum = posSum
		else:
			S.append(-1)
			minSum = negSum
		Sminsum.append(minSum)

	print 'combination algo:', S
	show_sum = []
	sums = 0
	for i in range(len(ar)):
		sums += ar[i] * S[i]
		show_sum.append(sums)
	print 'combination algo:', show_sum	


	return minSum

def randomWalks(ar):
	sums = 0
	Srandones = []

	for i in range(len(ar)):

		randone = random.randint(-1, 1)
		while randone == 0:
			randone = random.randint(-1, 1)
		
		Srandones.append(randone)
		sums += ar[i] * randone

	print ar
	print Srandones
	return abs(sums)

def showCombinations(ar):
	sums = 0
	finSums = 20000
	finComb = []
	iterations = 0
	for combination in product([-1, 1], repeat = len(ar)):
		iterations += 1
		for i in range(len(ar)):
			sums += combination[i] * ar[i]
		# print ar
		# print combination
		# print finSums, sums
		if abs(sums) < abs(finSums):
			finSums = abs(sums)
			finComb = list(combination)
		sums = 0
	print 'iterations:', iterations
	print 'combination perm:', finComb
	show_sum = []
	for i in range(len(ar)):
		sums += ar[i] * finComb[i]
		show_sum.append(sums)
	print 'combination perm:', show_sum	
	return finSums


A = [1, 5, 2, -2]
# A = [-100, -1200, -1, -1 ,-1, -1, -1, -1, -1, -1, -1]
A = [random.randint(-100, 100) for i in range(2)]

A = [85,	114,	98,	55,	-4]

print A

print solution(A)
print showCombinations(A)

# for combination in product([-1, 1], repeat = 3):
# 	print combination