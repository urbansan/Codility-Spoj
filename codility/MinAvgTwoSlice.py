from __future__ import division

def solution(ar):
	sums = [0]* (len(ar) + 1)

	lpos = 0
	r_lpos = 0
	minavg = 100000
	lavg = 0
	ravg = 0

	for i in range(len(ar)):
		sums[i+1] += sums[i] + ar[i]
		if i > 1:
			lavg = (sums[i+1] - sums[lpos]) / (i+1-lpos)
			ravg = (sums[i+1] - sums[i-1]) / 2.
			print lavg, ravg, minavg
			if lavg <= ravg:
				if lavg < minavg:
					minavg = lavg
					r_lpos = lpos
			else:
				lpos = i - 1
				if ravg < minavg:
					minavg = ravg
					r_lpos = lpos

	return r_lpos




A = [4, 2, 2, 5, 1, 5, 8]
# A = [4,2,2,5,1,2,1,5,3,3,4]
# A = [10	,20,	50,	-20,	4,	100,	-100	,200	,-4]
print solution(A)