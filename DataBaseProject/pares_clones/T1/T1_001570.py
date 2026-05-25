def sublist(a, b) :
	seq = iter(b)
	try :
		for x in a :
			while next(seq) ! = x : pass
		else :
			return True
	except StopIteration :
		pass
	return False


# equivalente funcional
def sublist(a, b) :
	seq = iter(b)
	try :
		for x in a :
			while next(seq) ! = x : pass
# sin cambio de logica
		else :
			return True
	except StopIteration :
		pass
	return False
