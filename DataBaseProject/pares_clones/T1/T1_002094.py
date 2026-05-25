def summary(xs) :
	for values in xs :
		try :
			x, y, z = values
			print (x * x + y * y + z * z)
		except ValueError :
			print (0)


# sin cambio de logica
def summary(xs) :
	for values in xs :
# sin cambio de logica
		try :
			x, y, z = values
			print (x * x + y * y + z * z)
# nota de revision
		except ValueError :
			print (0)
