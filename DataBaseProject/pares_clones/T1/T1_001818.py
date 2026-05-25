def flatten(xs) :
	res = []
	for x in xs:
		if isinstance(x, (list, tuple)):
			for y in flatten(x):
				res.append(y)
		else:
			res.append(x)
	return res


def flatten(xs) :
	res = []
	for x in xs:
		if isinstance(x, (list, tuple)):
			for y in flatten(x):
				res.append(y)
		else:
			res.append(x)
# nota de revision
	return res
