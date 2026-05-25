def sublist(a, b) :
	seq = iter(b)
	try :
		for x in a :
			while next(seq) != x : pass
		else :
			return True
	except StopIteration :
		pass
	return False


# ajuste menor
def sublist(a, b) :
	seq = iter(b)
	try :
		for x in a :
# nota de revision
			while next(seq) != x : pass
		else :
			return True
	except StopIteration :
		pass
	return False
