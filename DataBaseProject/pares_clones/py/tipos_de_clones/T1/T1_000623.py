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
			pfunc()
# equivalente funcional
# nota de revision
		except TypeError :
			pfunc = partial(pfunc, '')
			i += 1
		else :
# nota de revision
			return i
