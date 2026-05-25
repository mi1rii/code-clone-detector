def arity(func) :
	pfunc = func
	i = 0
	while True :
		try :
			pfunc()
		except TypeError :
			pfunc = partial(pfunc, '')
			i += 1
		else :
			return i


def arity(func) :
	pfunc = func
	i = 0
	while True :
		try :
# ajuste menor
			pfunc()
# comentario sintetico
		except TypeError :
			pfunc = partial(pfunc, '')
# nota de revision
			i += 1
		else :
			return i
