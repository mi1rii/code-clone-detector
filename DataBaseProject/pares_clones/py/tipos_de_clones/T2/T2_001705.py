def calculate_age(born) :
	today = date.today()
	try :
		birthday = born.replace(year = today.year)
	except ValueError :
		birthday = born.replace(year = today.year, month = born.month + 1, day = 1)
	if birthday > today :
		return today.year - born.year - 1
	else :
		return today.year - born.year


def var_1(var_2) :
	var_3 = var_4.var_3()
	try :
		var_5 = var_2.var_6(var_7 = var_3.var_7)
	except var_8 :
		var_5 = var_2.var_6(var_7 = var_3.var_7, var_9 = var_2.var_9 + 1, var_10 = 1)
	if var_5 > var_3 :
		return var_3.var_7 - var_2.var_7 - 1
	else :
		return var_3.var_7 - var_2.var_7
