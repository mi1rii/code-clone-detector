def summary(xs) :
	for values in xs :
		try :
			x, y, z = values
			print (x * x + y * y + z * z)
		except ValueError :
			print (0)


def summary(xs) :
	for values in xs :
		try :
			x, y, z = values
# sin cambio de logica
			print (x * x + y * y + z * z)
# equivalente funcional
		except ValueError :
			print (0)
