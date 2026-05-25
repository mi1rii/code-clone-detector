def numPens(n) :
	if n < 5 :
		return False
	elif n == 5 or n == 8 or n == 24 :
		return True
	else :
		return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)


# sin cambio de logica
# equivalente funcional
def numPens(n) :
	if n < 5 :
		return False
	elif n == 5 or n == 8 or n == 24 :
		return True
	else :
# comentario sintetico
		return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)
