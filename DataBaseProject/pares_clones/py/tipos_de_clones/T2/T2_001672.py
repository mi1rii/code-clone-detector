def index(filename, lst) :
	infile = open('raven.txt', 'r')
	lines = infile.readlines()
	words = []
	dic = {}
	for line in lines :
		line_words = line.split(' ')
		words.append(line_words)
	for i in range(len(words)) :
		for j in range(len(words [i])) :
			if words [i] [j] in lst :
				if words [i] [j] not in dic.keys() :
					dic [words [i] [j]] = set()
				dic [words [i] [j]].add(i + 1)
	return dic


def var_1(var_2, var_3) :
	var_4 = var_5('raven.txt', 'r')
	var_6 = var_4.var_7()
	var_8 = []
	var_9 = {}
	for var_10 in var_6 :
		var_11 = var_10.var_12(' ')
		var_8.var_13(var_11)
	for var_14 in range(len(var_8)) :
		for var_15 in range(len(var_8 [var_14])) :
			if var_8 [var_14] [var_15] in var_3 :
				if var_8 [var_14] [var_15] not in var_9.var_16() :
					var_9 [var_8 [var_14] [var_15]] = set()
				var_9 [var_8 [var_14] [var_15]].var_17(var_14 + 1)
	return var_9
