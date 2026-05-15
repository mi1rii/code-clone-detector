def get_most_ooo_word(words) :
	words = words [0].split()
	most = [words [0]]
	for word in words [1 :] :
		if word.count('o') > most [0].count('o') :
			most = [word]
		elif word.count('o') == most [0].count('o') :
			most.append(word)
	return most


def var_1(var_2) :
	var_2 = var_2 [0].var_3()
	var_4 = [var_2 [0]]
	for var_5 in var_2 [1 :] :
		if var_5.var_6('o') > var_4 [0].var_6('o') :
			var_4 = [var_5]
		elif var_5.var_6('o') == var_4 [0].var_6('o') :
			var_4.var_7(var_5)
	return var_4
