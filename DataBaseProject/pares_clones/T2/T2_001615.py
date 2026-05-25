def num_input(s) :
	while True :
		try :
			return decimal.Decimal(raw_input(s))
		except decimal.InvalidOperation as e :
			print(e.message)


def var_1(var_2) :
	while True :
		try :
			return var_3.var_4(var_5(var_2))
		except var_3.var_6 as var_7 :
			print(var_7.var_8)
