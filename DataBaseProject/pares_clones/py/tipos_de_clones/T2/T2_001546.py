def scan(words) :
	result = []
	for word in words.split() :
		found_category = 'error'
		for category, category_lexicon in _LEXICON.items() :
			if word in category_lexicon :
				found_category = category
				break
		result.append((found_category, word))
	return result


def var_1(var_2) :
	var_3 = []
	for var_4 in var_2.var_5() :
		var_6 = 'error'
		for var_7, var_8 in var_9.var_10() :
			if var_4 in var_8 :
				var_6 = var_7
				break
		var_3.var_11((var_6, var_4))
	return var_3
