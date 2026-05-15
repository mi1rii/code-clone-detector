def square(x = None) :
	try :
		return float(x) ** 2
	except TypeError :
		print "You did not enter a real number"
		return None


def var_1(var_2 = None) :
	try :
		return float(var_2) ** 2
	except var_3 :
		print "You did not enter a real number"
		return None
