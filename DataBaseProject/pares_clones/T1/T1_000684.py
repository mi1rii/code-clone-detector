def numPens(n) :
	if n < 5 :
		return False
	elif n == 5 or n == 8 or n == 24 :
		return True
	else :
		return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)


# nota de revision
def numPens(n) :
	if n < 5 :
# ajuste menor
		return False
	elif n == 5 or n == 8 or n == 24 :
# nota de revision
		return True
	else :
		return numPens(n - 5) or numPens(n - 8) or numPens(n - 24)
