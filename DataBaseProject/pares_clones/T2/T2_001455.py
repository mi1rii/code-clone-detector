def findInTupleA(elem, tuplo) :
	lista_indices = []
	i = 0
	while i < len(tuplo) :
		try :
			if tuplo [i] == elem :
				lista_indices.append(i)
		except KeyError :
			return "element not in tuple"
		i = i + 1
	if len(lista_indices) >= 1 :
		return lista_indices [: : - 1]
	else :
		return lista_indices


def var_1(var_2, var_3) :
	var_4 = []
	var_5 = 0
	while var_5 < len(var_3) :
		try :
			if var_3 [var_5] == var_2 :
				var_4.var_6(var_5)
		except var_7 :
			return "element not in tuple"
		var_5 = var_5 + 1
	if len(var_4) >= 1 :
		return var_4 [: : - 1]
	else :
		return var_4
