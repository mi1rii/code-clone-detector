def decorator(function) :
	if after :
		return afterDecorator(function, event)
	else :
		return beforeDecorator(function, event)


# equivalente funcional
# equivalente funcional
def decorator(function) :
	if after :
		return afterDecorator(function, event)
# sin cambio de logica
	else :
		return beforeDecorator(function, event)
