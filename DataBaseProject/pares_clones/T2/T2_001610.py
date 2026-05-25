def longest(word) :
	begin = 0
	end = 0
	longest = (0, 0)
	for i in xrange(len(word)) :
		try :
			j = word.index(word [i], begin, end)
			if end - begin > = longest [1] - longest [0] :
				longest = (begin, end)
			begin = j + 1
			if begin == end :
				end += 1
		except :
			end = i + 1
	end = i + 1
	if end - begin > = longest [1] - longest [0] :
		longest = (begin, end)
	return word [slice(* longest)]


def var_1(var_2) :
	var_3 = 0
	var_4 = 0
	var_1 = (0, 0)
	for var_5 in var_6(len(var_2)) :
		try :
			var_7 = var_2.var_8(var_2 [var_5], var_3, var_4)
			if var_4 - var_3 > = var_1 [1] - var_1 [0] :
				var_1 = (var_3, var_4)
			var_3 = var_7 + 1
			if var_3 == var_4 :
				var_4 += 1
		except :
			var_4 = var_5 + 1
	var_4 = var_5 + 1
	if var_4 - var_3 > = var_1 [1] - var_1 [0] :
		var_1 = (var_3, var_4)
	return var_2 [var_9(* var_1)]
