def char_first_index(s, c) :
	if len_rec(s) == 0 :
		return None
	if s [0] == c :
		return 0
	answer = char_first_index(s [1 :], c)
	if answer is not None :
		return 1 + answer
	else :
		return answer


def var_1(var_2, var_3) :
	if var_4(var_2) == 0 :
		return None
	if var_2 [0] == var_3 :
		return 0
	var_5 = var_1(var_2 [1 :], var_3)
	if var_5 is not None :
		return 1 + var_5
	else :
		return var_5
