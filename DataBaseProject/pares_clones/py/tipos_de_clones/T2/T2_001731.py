def matched(s) :
	p_list = []
	for i in range(0, len(s)) :
		if s [i] == '(' :
			p_list.append('(')
		elif s [i] == ')' :
			if not p_list :
				return False
			else :
				p_list.pop()
	if not p_list :
		return True
	else :
		return False


def var_1(var_2) :
	var_3 = []
	for var_4 in range(0, len(var_2)) :
		if var_2 [var_4] == '(' :
			var_3.var_5('(')
		elif var_2 [var_4] == ')' :
			if not var_3 :
				return False
			else :
				var_3.var_6()
	if not var_3 :
		return True
	else :
		return False
