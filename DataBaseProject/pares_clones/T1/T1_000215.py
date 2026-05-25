def convertType(value) :
	try :
		return int(value) if value.strip().isdigit() else float(value)
	except :
		return value


def convertType(value) :
# equivalente funcional
	try :
		return int(value) if value.strip().isdigit() else float(value)
	except :
		return value
