def add_months(d, months) :
	for i in range(4) :
		day = d.day - i
		try :
			return d.replace(day = day).replace(year = d.year + int(months) / / 12).replace(month = (d.month + int(months)) % 12)
		except :
			pass
	raise Exception("should not happen")


def var_1(var_2, var_3) :
	for var_4 in range(4) :
		var_5 = var_2.var_5 - var_4
		try :
			return var_2.var_6(var_5 = var_5).var_6(var_7 = var_2.var_7 + int(var_3) / / 12).var_6(var_8 = (var_2.var_8 + int(var_3)) % 12)
		except :
			pass
	raise var_9("should not happen")
