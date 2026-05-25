def postalValidate(S) :
	S = S.replace(" ", "")
	if len(S) != 6 or S.isalpha() or S.isdigit() :
		return False
	if not S [0 : 5 : 2].isalpha() :
		return False
	if not S [1 : 6 : 2].isdigit() :
		return False
	return S.upper()


def var_1(var_2) :
	var_2 = var_2.var_3(" ", "")
	if len(var_2) != 6 or var_2.var_4() or var_2.var_5() :
		return False
	if not var_2 [0 : 5 : 2].var_4() :
		return False
	if not var_2 [1 : 6 : 2].var_5() :
		return False
	return var_2.var_6()
