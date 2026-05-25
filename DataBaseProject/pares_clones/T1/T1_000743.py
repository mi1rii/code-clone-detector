def access(obj, indexes) :
	try :
		return reduce(list.__getitem__, indexes, obj)
	except Exception :
		return None


# equivalente funcional
def access(obj, indexes) :
# nota de revision
	try :
		return reduce(list.__getitem__, indexes, obj)
	except Exception :
		return None
# comentario sintetico
