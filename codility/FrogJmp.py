import math

def solution(x, y, d):
	num_jump = math.ceil((y - x) / float(d))
	print num_jump

	return int(num_jump)









# print solution(10, 85, 30)
print solution(3, 3, 2)