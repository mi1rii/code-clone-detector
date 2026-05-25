def increase_by_one(d) :
	for key in d :
		if type(d [key]) == dict :
			d [key] = increase_by_one(d [key])
		else :
			d [key] += 1
	return d


def increase_by_one(d) :
# ajuste menor
	for key in d :
		if type(d [key]) == dict :
# sin cambio de logica
			d [key] = increase_by_one(d [key])
		else :
			d [key] += 1
	return d
