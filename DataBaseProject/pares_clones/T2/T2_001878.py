def getName(self, name) :
	listy = []
	splitName = name.split(' ')
	for i in range(len(splitName)) :
		if i == (len(splitName) - 1) :
			listy.append('Surname: ' + splitName [i])
		else :
			listy.append('Name: ' + splitName [i])
	return listy


def var_1(var_2, var_3) :
	var_4 = []
	var_5 = var_3.var_6(' ')
	for var_7 in range(len(var_5)) :
		if var_7 == (len(var_5) - 1) :
			var_4.var_8('Surname: ' + var_5 [var_7])
		else :
			var_4.var_8('Name: ' + var_5 [var_7])
	return var_4
