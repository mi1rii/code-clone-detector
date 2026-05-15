def permutations(string) :
	if len(string) == 1 :
		return string
	recursive_perms = []
	for c in string :
		for perm in permutations(string.replace(c, '', 1)) :
			revursive_perms.append(c + perm)
	return set(revursive_perms)


def var_1(var_2) :
	if len(var_2) == 1 :
		return var_2
	var_3 = []
	for var_4 in var_2 :
		for var_5 in var_1(var_2.var_6(var_4, '', 1)) :
			var_7.var_8(var_4 + var_5)
	return set(var_7)
