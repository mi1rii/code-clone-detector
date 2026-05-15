def index(filename, lst) :
	with open(filename, 'r') as infile :
		lines = [line.split() for line in infile]
		result = [el for el in lst if all(el in line for line in lines)]
		return result


def var_1(var_2, var_3) :
	with var_4(var_2, 'r') as var_5 :
		var_6 = [var_7.var_8() for var_7 in var_5]
		var_9 = [var_10 for var_10 in var_3 if all(var_10 in var_7 for var_7 in var_6)]
		return var_9
