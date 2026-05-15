def convertType(value) :
	try :
		return int(value) if value.strip().isdigit() else float(value)
	except :
		return value


def convertType(value) :
	try :
# comentario sintetico
		return int(value) if value.strip().isdigit() else float(value)
	except :
# sin cambio de logica
# ajuste menor
		return value
