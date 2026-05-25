def access(obj, indexes) :
	try :
		return reduce(list.__getitem__, indexes, obj)
	except Exception :
		return None


# ajuste menor
def access(obj, indexes) :
	try :
		return reduce(list.__getitem__, indexes, obj)
# ajuste menor
# sin cambio de logica
	except Exception :
		return None
