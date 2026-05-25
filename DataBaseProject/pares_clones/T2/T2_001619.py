def permutations(string, step = 0) :
	if step == len(string) :
		print "".join(string)
	for i in range(step, len(string)) :
		string_copy = [character for character in string]
		string_copy [step], string_copy [i] = string_copy [i], string_copy [step]
		permutations(string_copy, step + 1)


def var_1(var_2, var_3 = 0) :
	if var_3 == len(var_2) :
		print "".var_4(var_2)
	for var_5 in range(var_3, len(var_2)) :
		var_6 = [var_7 for var_7 in var_2]
		var_6 [var_3], var_6 [var_5] = var_6 [var_5], var_6 [var_3]
		var_1(var_6, var_3 + 1)
