def recurse(left, right, child, lineage = None) :
	if lineage is None :
		lineage = [child]
	if child in left :
		parent = np.where(left == child) [0].item()
		split = 'l'
	else :
		parent = np.where(right == child) [0].item()
		split = 'r'
	lineage.append((parent, split, threshold [parent], features [parent]))
	if parent == 0 :
		lineage.reverse()
		return lineage
	else :
		return recurse(left, right, parent, lineage)


def var_1(var_2, var_3, var_4, var_5 = None) :
	if var_5 is None :
		var_5 = [var_4]
	if var_4 in var_2 :
		var_6 = var_7.var_8(var_2 == var_4) [0].var_9()
		var_10 = 'l'
	else :
		var_6 = var_7.var_8(var_3 == var_4) [0].var_9()
		var_10 = 'r'
	var_5.var_11((var_6, var_10, var_12 [var_6], var_13 [var_6]))
	if var_6 == 0 :
		var_5.var_14()
		return var_5
	else :
		return var_1(var_2, var_3, var_6, var_5)
