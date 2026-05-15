def token_list_count(df) :
	dfIterrows = df.iterrows()
	for i, t in dfIterrows :
		list_a = 0
		list_b = 0
		tTokens = t ['tokens']
		for tok in tTokens :
			if tok in seta : list_a += 1
			elif tok in setb : list_b += 1
		df.loc [i, 'token_count'] = int(len(t ['tokens']))
		df.loc [i, 'lista_count'] = int(list_a)
		df.loc [i, 'listb_count'] = int(list_b)
		if i % 25000 == 0 : print ('25k more processed...')
	return df


def var_1(var_2) :
	var_3 = var_2.var_4()
	for var_5, var_6 in var_3 :
		var_7 = 0
		var_8 = 0
		var_9 = var_6 ['tokens']
		for var_10 in var_9 :
			if var_10 in var_11 : var_7 += 1
			elif var_10 in var_12 : var_8 += 1
		var_2.var_13 [var_5, 'token_count'] = int(len(var_6 ['tokens']))
		var_2.var_13 [var_5, 'lista_count'] = int(var_7)
		var_2.var_13 [var_5, 'listb_count'] = int(var_8)
		if var_5 % 25000 == 0 : print ('25k more processed...')
	return var_2
