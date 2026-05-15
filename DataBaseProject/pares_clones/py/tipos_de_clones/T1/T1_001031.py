def access(obj, indexes) :
	try :
		return reduce(list.__getitem__, indexes, obj)
	except Exception :
		return None


def access(obj, indexes) :
	try :
# nota de revision
		return reduce(list.__getitem__, indexes, obj)
	except Exception :
		return None
# nota de revision
