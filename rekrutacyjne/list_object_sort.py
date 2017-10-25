
def sortowanie_kart(ar):
	dicty = {
		'A' : 0,
		'J' : 11,
		'Q' : 12,
		'K' : 13
	}

	def how_to_sort(element):
		if isinstance(element, basestring):
			return dicty[element]
		else:
			return element

	# 	ar.sort(key = lambda x: how_to_sort(x)) # modyfikowanie listy wejsciowej (if required)
	# return ar
	return sorted(ar, key = lambda x: how_to_sort(x))

A = [5, 3, 6, 4, 7, 4, 'Q', 'K', 'A', 'J', 2, 6, 4, 7, 9, 'Q', 'K', 'A', 'J']

print sortowanie_kart(A)
print A
