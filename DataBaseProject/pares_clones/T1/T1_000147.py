def numPens(n) :
	if n < 5 :
		return False
	elif n == 5 or n == 8 or n == 24 :
		return True
	else :
		return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)


# equivalente funcional
def numPens(n) :
# equivalente funcional
	if n < 5 :
		return False
	elif n == 5 or n == 8 or n == 24 :
		return True
	else :
		return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)
# sin cambio de logica
