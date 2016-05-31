
def solution(ar):
	ar.sort()
	last_int = 0
	for i in range(len(ar)):
		if(ar[i]) > 0:
			if ar[i] == last_int:
				pass
			elif ar[i]-1 == last_int:
				last_int += 1
			else:
				return last_int + 1
		else:
			pass

	return last_int + 1



# A = [1, 3, 6, 4, 1, 2]
# A = [0]
A = [-20, -121, -2131, -12] #,  3, 6, 4, 1, 2]

print solution(A)