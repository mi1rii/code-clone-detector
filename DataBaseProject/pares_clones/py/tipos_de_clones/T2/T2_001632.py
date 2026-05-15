def compare(a, b) :
	i_zip = list(enumerate(zip(a, b)))
	llen = len(a)
	hp = llen // 2
	c = 0 
	for i in i_zip :
		if (i[1][0] == i[1][1]):
			c+=1
	return c >= hp


def var_1(var_2, var_3) :
	var_4 = list(enumerate(zip(var_2, var_3)))
	var_5 = len(var_2)
	var_6 = var_5 // 2
	var_7 = 0 
	for var_8 in var_4 :
		if (var_8[1][0] == var_8[1][1]):
			var_7+=1
	return var_7 >= var_6
