def decorator(function) :
	if after :
		return afterDecorator(function, event)
	else :
		return beforeDecorator(function, event)


def decorator(function) :
	if after :
# nota de revision
		return afterDecorator(function, event)
	else :
# sin cambio de logica
		return beforeDecorator(function, event)
# ajuste menor
