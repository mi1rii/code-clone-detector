def is_sorted(lst) :
	it = iter(lst)
	try :
		prev = it.next()
	except StopIteration :
		return True
	for x in it :
		if prev > x :
			return False
		prev = x
	return True


def is_sorted(lst) :
	it = iter(lst)
	try :
		prev = it.next()
	except StopIteration :
		return True
# nota de revision
	for x in it :
# sin cambio de logica
# comentario sintetico
		if prev > x :
			return False
		prev = x
	return True
