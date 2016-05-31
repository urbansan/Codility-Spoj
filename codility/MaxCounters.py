
def solution1(x, ar):
	counter = [0 for i in range(x)]
	for i in range(len(ar)):
		if ar[i] > x:
			maxis = max(counter)
			for j in range(x):
				counter[j] = maxis
		else:
			counter[ar[i]-1] += 1
	return counter	

def solution(x, ar):
	maxis = 0
	current_max = 0
	counter = [0 for i in range(x)]
	for i in range(len(ar)):
		if ar[i] > x:
			maxis = current_max
		elif counter[ar[i]-1] < maxis:
			counter[ar[i]-1] = maxis
			counter[ar[i]-1] += 1
			current_max = max(current_max, counter[ar[i]-1])
		else:
			counter[ar[i]-1] += 1
			current_max = max(current_max, counter[ar[i]-1])
	for j in range(x):
		if counter[j] < maxis:
			counter[j] = maxis
	return counter	


A = [3, 4, 4, 6, 1, 4, 4]
# A = [3, 4, 4, 4]
# A = [3, 4, 4, 6, 1, 4, 4]
print solution(5, A)