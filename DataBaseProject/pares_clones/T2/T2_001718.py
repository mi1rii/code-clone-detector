def flatten(container) :
	for i in container :
		if isinstance(i, (list, tuple)) :
			for j in flatten(i) :
				yield j
		else :
			yield i


def var_1(var_2) :
	for var_3 in var_2 :
		if isinstance(var_3, (list, tuple)) :
			for var_4 in var_1(var_3) :
				yield var_4
		else :
			yield var_3
