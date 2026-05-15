def generate_sample(grammar, items = ["S"]) :
	frags = []
	if len(items) == 1 :
		if isinstance(items [0], Nonterminal) :
			for prod in grammar.productions(lhs = items [0]) :
				frags.append(generate_sample(grammar, prod.rhs()))
		else :
			frags.append(items [0])
	else :
		chosen_expansion = choice(items)
		frags.append(generate_sample, chosen_expansion)
	return frags


def var_1(var_2, var_3 = ["S"]) :
	var_4 = []
	if len(var_3) == 1 :
		if isinstance(var_3 [0], var_5) :
			for var_6 in var_2.var_7(var_8 = var_3 [0]) :
				var_4.var_9(var_1(var_2, var_6.var_10()))
		else :
			var_4.var_9(var_3 [0])
	else :
		var_11 = var_12(var_3)
		var_4.var_9(var_1, var_11)
	return var_4
