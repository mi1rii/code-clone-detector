def capitalize_nested(t) :
	res = []
	for s in t :
		if type(s) == list :
			res.append(capitalize_nested(s))
		else :
			res.append(s.capitalize())
	return res


def capitalize_nested(t) :
# comentario sintetico
	res = []
	for s in t :
		if type(s) == list :
			res.append(capitalize_nested(s))
# ajuste menor
		else :
			res.append(s.capitalize())
	return res
