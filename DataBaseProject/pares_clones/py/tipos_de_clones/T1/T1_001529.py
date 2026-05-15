def decorator(function) :
	if after :
		return afterDecorator(function, event)
	else :
		return beforeDecorator(function, event)


def decorator(function) :
	if after :
# ajuste menor
		return afterDecorator(function, event)
# equivalente funcional
	else :
		return beforeDecorator(function, event)
