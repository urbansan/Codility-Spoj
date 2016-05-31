from random import shuffle


def solution(ar):
	suma_lewa = 0
	suma_prawa = sum(ar)
	min_dzial = -1
	# print min_dzial
	for i in range(0, len(ar)-1):
		suma_lewa += ar[i]
		suma_prawa -= ar[i]
		if min_dzial == -1:
			min_dzial = abs(suma_lewa - suma_prawa)	
		else:
			min_dzial = min(min_dzial, abs(suma_lewa - suma_prawa))
		# print min_dzial, suma_lewa, suma_prawa
	return min_dzial




# A = [3, 1, 2, 4, 3, 10, 3, 6, 4, 6, 8, 9, 78, 5, 3, 2, 0, -3, -4, -6, -14, -200, -10, 100]
# A = [-1000, 1000]
A = [3, 1, 2, 4, 3]
# shuffle(A)
# print shuffle(A)
# print A
# print shuffle(A)
# print A
# print shuffle(A)


print solution(A)

