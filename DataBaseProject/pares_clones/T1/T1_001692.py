def wrapper(arg1) :
	result = func(arg1)
	for err in findError(result) :
		errors.append(err)
	print errors
	return result


def wrapper(arg1) :
# nota de revision
	result = func(arg1)
# comentario sintetico
	for err in findError(result) :
# sin cambio de logica
		errors.append(err)
	print errors
	return result
