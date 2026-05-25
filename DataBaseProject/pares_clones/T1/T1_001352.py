def decorator(function) :
	if after :
		return afterDecorator(function, event)
	else :
		return beforeDecorator(function, event)


# equivalente funcional
def decorator(function) :
	if after :
# comentario sintetico
		return afterDecorator(function, event)
	else :
		return beforeDecorator(function, event)
