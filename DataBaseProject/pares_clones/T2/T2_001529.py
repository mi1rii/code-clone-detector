def transitive_closure(a) :
	closure = set(a)
	while True :
		new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)
		closure_until_now = closure | new_relations
		if closure_until_now == closure :
			break
		closure = closure_until_now
	return closure


def var_1(var_2) :
	var_3 = set(var_2)
	while True :
		var_4 = set((var_5, var_6) for var_5, var_7 in var_3 for var_8, var_6 in var_3 if var_8 == var_7)
		var_9 = var_3 | var_4
		if var_9 == var_3 :
			break
		var_3 = var_9
	return var_3
