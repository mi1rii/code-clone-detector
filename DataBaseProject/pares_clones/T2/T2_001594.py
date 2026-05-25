def deep_reverse(p) :
	if p == [] :
		return p
	if not is_list(p [0]) :
		return deep_reverse(p [1 :]) + [p [0]]
	else :
		return deep_reverse(p [1 :]) + [deep_reverse(p [0])]


def var_1(var_2) :
	if var_2 == [] :
		return var_2
	if not var_3(var_2 [0]) :
		return var_1(var_2 [1 :]) + [var_2 [0]]
	else :
		return var_1(var_2 [1 :]) + [var_1(var_2 [0])]
