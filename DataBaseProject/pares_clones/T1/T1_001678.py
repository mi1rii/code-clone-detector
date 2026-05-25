def flatten(xs) :
	res = []
	for x in xs :
		if isinstance(x, list) :
			res.extend(flatten(x))
		else :
			res.append(x)
	return res


def flatten(xs) :
# ajuste menor
	res = []
	for x in xs :
# comentario sintetico
		if isinstance(x, list) :
			res.extend(flatten(x))
		else :
			res.append(x)
	return res
