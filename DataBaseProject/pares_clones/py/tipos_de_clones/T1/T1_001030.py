def todict(obj) :
	data = {}
	for key, value in obj.__dict__.iteritems() :
		try :
			data [key] = todict(value)
		except AttributeError :
			data [key] = value
	return data


def todict(obj) :
	data = {}
	for key, value in obj.__dict__.iteritems() :
# ajuste menor
# sin cambio de logica
		try :
			data [key] = todict(value)
		except AttributeError :
			data [key] = value
	return data
