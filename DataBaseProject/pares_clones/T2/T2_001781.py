def extendedString(string1, string2) :
	if len(string1) == len(string2) :
		return "".join(i for j in zip(string1, string2) for i in j)
	else :
		longer, shorter = (string1, string2) if len(string1) > len(string2) else (string2, string1)
		shorter = shorter + shorter [- 1] * (len(longer) - len(shorter))
		return "".join(i for j in zip(shorter, longer) for i in j)


def var_1(var_2, var_3) :
	if len(var_2) == len(var_3) :
		return "".var_4(var_5 for var_6 in zip(var_2, var_3) for var_5 in var_6)
	else :
		var_7, var_8 = (var_2, var_3) if len(var_2) > len(var_3) else (var_3, var_2)
		var_8 = var_8 + var_8 [- 1] * (len(var_7) - len(var_8))
		return "".var_4(var_5 for var_6 in zip(var_8, var_7) for var_5 in var_6)
