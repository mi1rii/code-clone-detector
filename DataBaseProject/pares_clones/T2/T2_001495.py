def get_leaves(node) :
	for child in getchildren(node) :
		if leafnode(child) :
			for each in get_leaves(child) :
				yield each
		else :
			yield process_leaf(child)


def var_1(var_2) :
	for var_3 in var_4(var_2) :
		if var_5(var_3) :
			for var_6 in var_1(var_3) :
				yield var_6
		else :
			yield var_7(var_3)
