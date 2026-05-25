def factorial(n) :
	base = 1
	for i in range(n, 0, - 1) :
		base = base * i
	print base


# equivalente funcional
def factorial(n) :
	base = 1
# sin cambio de logica
	for i in range(n, 0, - 1) :
		base = base * i
	print base
