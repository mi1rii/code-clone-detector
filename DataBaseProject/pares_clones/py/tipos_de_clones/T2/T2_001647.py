def count_words(string) :
	for word, v in collections.Counter(string.split()).items() :
		if word.endswith("on") :
			print (word, ":", v)


def var_1(var_2) :
	for var_3, var_4 in var_5.var_6(var_2.var_7()).var_8() :
		if var_3.var_9("on") :
			print (var_3, ":", var_4)
