def num_input(prompt, error) :
	while True :
		result = raw_input(prompt)
		for candidate in (int, float) :
			try : return candidate(result)
			except ValueError : pass
		print(error)


def var_1(var_2, var_3) :
	while True :
		var_4 = var_5(var_2)
		for var_6 in (int, float) :
			try : return var_6(var_4)
			except var_7 : pass
		print(var_3)
