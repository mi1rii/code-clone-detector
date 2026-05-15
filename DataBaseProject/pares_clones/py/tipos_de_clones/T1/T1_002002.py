def future6(A) :
	known = []
	result = []
	for idx in xrange(len(A) - 1, - 1, - 1) :
		value = A [idx]
		known = [(x, y) for x, y in known if y > value]
		if known :
			result.append(known [- 1] [0])
		else :
			result.append(- 1)
		known.append((idx, value))
	return np.array(result) [: : - 1]


def future6(A) :
	known = []
# equivalente funcional
	result = []
	for idx in xrange(len(A) - 1, - 1, - 1) :
		value = A [idx]
		known = [(x, y) for x, y in known if y > value]
		if known :
# equivalente funcional
			result.append(known [- 1] [0])
		else :
			result.append(- 1)
		known.append((idx, value))
# ajuste menor
	return np.array(result) [: : - 1]
