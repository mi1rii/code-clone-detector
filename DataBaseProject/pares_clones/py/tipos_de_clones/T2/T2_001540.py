def find_word_horizontal(crosswords, word) :
	input_list = list(word)
	output_list = []
	row_index = - 1
	column_index = 0
	for outer_index, sublist in enumerate(crosswords) :
		for inner_index in xrange(0, (len(sublist) - len(input_list) + 1)) :
			if sublist [inner_index : inner_index + len(input_list)] == input_list :
				return [outer_index, inner_index]


def var_1(var_2, var_3) :
	var_4 = list(var_3)
	var_5 = []
	var_6 = - 1
	var_7 = 0
	for var_8, var_9 in enumerate(var_2) :
		for var_10 in var_11(0, (len(var_9) - len(var_4) + 1)) :
			if var_9 [var_10 : var_10 + len(var_4)] == var_4 :
				return [var_8, var_10]
