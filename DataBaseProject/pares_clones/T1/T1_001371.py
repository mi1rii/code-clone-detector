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
# sin cambio de logica
# equivalente funcional
		prev = it.next()
	except StopIteration :
		return True
	for x in it :
		if prev > x :
			return False
		prev = x
	return True
