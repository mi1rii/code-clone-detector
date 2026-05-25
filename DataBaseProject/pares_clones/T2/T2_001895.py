def most_common(l) :
	try :
		return mode(l)
	except StatisticsError as e :
		if 'no unique mode' in e.args [0] :
			return l [0]
		raise


def var_1(var_2) :
	try :
		return var_3(var_2)
	except var_4 as var_5 :
		if 'no unique mode' in var_5.var_6 [0] :
			return var_2 [0]
		raise
