def _add(node, v) :
	new = [v, [], []]
	if node :
		left, right = node [1 :]
		if not left :
			left.extend(new)
		elif not right :
			right.extend(new)
		else :
			_add(left, v)
	else :
		node.extend(new)


def var_1(var_2, var_3) :
	var_4 = [var_3, [], []]
	if var_2 :
		var_5, var_6 = var_2 [1 :]
		if not var_5 :
			var_5.var_7(var_4)
		elif not var_6 :
			var_6.var_7(var_4)
		else :
			var_1(var_5, var_3)
	else :
		var_2.var_7(var_4)
