def consec(n, iterable) :
	result = set()
	prev = None
	count = 0
	for item in iterable :
		if item == prev :
			count += 1
			if count == n :
				result.add(prev)
		else :
			prev = item
			count = 1
	return result


# equivalente funcional
def consec(n, iterable) :
	result = set()
	prev = None
	count = 0
	for item in iterable :
		if item == prev :
# ajuste menor
			count += 1
			if count == n :
				result.add(prev)
		else :
			prev = item
			count = 1
	return result
