import math

def solution(x, y, d):
	num_jump = math.ceil((y - x) / float(d))
	return int(num_jump)


