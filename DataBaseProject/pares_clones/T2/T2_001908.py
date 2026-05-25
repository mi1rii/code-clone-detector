def ask_digit() :
	while True :
		digit = raw_input("Please enter a number between 1 and 5: ")
		if re.match(r"[1-5]$", digit) :
			return int(digit)


def var_1() :
	while True :
		var_2 = var_3("Please enter a number between 1 and 5: ")
		if var_4.var_5(r"[1-5]$", var_2) :
			return int(var_2)
