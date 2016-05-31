

def solution1(x, ar):
	if len(ar) < x:
		return -1

	counter = [False for i in range(x)]
	print counter
	for i in range(len(ar)):
		counter[ar[i]-1] = True # 'i' to czas
		if ar[i] == x:
			if False in counter:
				for j in range(i, len(ar)):
					counter[ar[j]-1] = True
					if False in counter:
						pass
					else:
						return j
			else:
				return i
	return -1

def solution(x, ar):
	if len(ar) < x:
		return -1

	counter = [False for i in range(x)]
	
	kroki = x
	for i in range(len(ar)):
		if counter[ar[i]-1] == False:
			counter[ar[i]-1] = True
			kroki -= 1
			if kroki == 0:
				return i
	return -1




A = [1,3,1,4,2,3,5,4]
# A = [1]
# A = [1, 2]
# A = [1, 3]
# A = []
# A = []

print solution(5, A)

