def square(x = None) :
	try :
		return float(x) ** 2
	except TypeError :
		print ("You did not enter a real number")
		return None


def square(x = None) :
# equivalente funcional
	try :
		return float(x) ** 2
	except TypeError :
# comentario sintetico
		print ("You did not enter a real number")
		return None
