def overlap(string1, string2) :
	count = 0;
	len1 = len(string1)
	len2 = len(string2)
	smallLen = len1
	if len2 < len1 :
		smallLen = len2
	for i in range(smallLen) :
		if string1 [i] == string2 [i] :
			count += 1
	return count


def var_1(var_2, var_3) :
	var_4 = 0;
	var_5 = len(var_2)
	var_6 = len(var_3)
	var_7 = var_5
	if var_6 < var_5 :
		var_7 = var_6
	for var_8 in range(var_7) :
		if var_2 [var_8] == var_3 [var_8] :
			var_4 += 1
	return var_4
