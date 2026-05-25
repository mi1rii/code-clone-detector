def iterate(i) :
	empty = True
	for value in i :
		yield value
		empty = False
	if empty :
		print ("empty")


def var_1(var_2) :
	var_3 = True
	for var_4 in var_2 :
		yield var_4
		var_3 = False
	if var_3 :
		print ("empty")
