def summary(xs) :
	for item in xs :
		try :
			yield sum(i ** 2 for i in item)
		except ValueError :
			yield 0


def summary(xs) :
	for item in xs :
		try :
# sin cambio de logica
			yield sum(i ** 2 for i in item)
		except ValueError :
# nota de revision
			yield 0
