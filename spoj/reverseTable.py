import sys


def no_exceptions(funx):
	def deco_funx(*args, **kwargs):
		try:
			funx(*args, **kwargs)
		except:
			pass
	return deco_funx

@no_exceptions
def reverse():
	num_tests = int(sys.stdin.read(2).strip())
	num_tests = min(num_tests, 100)
	for i in range(num_tests):
		test_len = int(sys.stdin.read(2).strip())
		test_len = min(test_len, 100)
		A = []
		for j in range(test_len):
			A.insert(0, sys.stdin.read(2).strip())
			if j >test_len:
				break

		if len(A) > 0:
			for j in range(len(A)):
				print A[j],

		print

def reverse_j():
	num_tests = int(sys.stdin.readline().split()[0])

	for i in range(num_tests):
		line_in = sys.stdin.readline().split()
		test_len = int(line_in.pop(0))

		line_in.reverse()

		if len(line_in) > 0:
			for j in range(len(line_in)):
				print line_in[j],

		print


reverse_j()			# if j >test_len:
			# 	break