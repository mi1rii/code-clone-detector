def all_pairs(lst) :
	if not lst :
		yield [tuple()]
	elif len(lst) == 1 :
		yield [tuple(lst)]
	elif len(lst) == 2 :
		yield [tuple(lst)]
	else :
		if len(lst) % 2 :
			for i in (None, True) :
				if i not in lst :
					lst = list(lst) + [i]
					PAD = i
					break
			else :
				while chr(i) in lst :
					i += 1
				PAD = chr(i)
				lst = list(lst) + [PAD]
		else :
			PAD = False
		a = lst [0]
		for i in range(1, len(lst)) :
			pair = (a, lst [i])
			for rest in all_pairs(lst [1 : i] + lst [i + 1 :]) :
				rv = [pair] + rest
				if PAD is not False :
					for i, t in enumerate(rv) :
						if PAD in t :
							rv [i] = (t [0],)
							break
				yield rv


def var_1(var_2) :
	if not var_2 :
		yield [tuple()]
	elif len(var_2) == 1 :
		yield [tuple(var_2)]
	elif len(var_2) == 2 :
		yield [tuple(var_2)]
	else :
		if len(var_2) % 2 :
			for var_3 in (None, True) :
				if var_3 not in var_2 :
					var_2 = list(var_2) + [var_3]
					var_4 = var_3
					break
			else :
				while var_5(var_3) in var_2 :
					var_3 += 1
				var_4 = var_5(var_3)
				var_2 = list(var_2) + [var_4]
		else :
			var_4 = False
		var_6 = var_2 [0]
		for var_3 in range(1, len(var_2)) :
			var_7 = (var_6, var_2 [var_3])
			for var_8 in var_1(var_2 [1 : var_3] + var_2 [var_3 + 1 :]) :
				var_9 = [var_7] + var_8
				if var_4 is not False :
					for var_3, var_10 in enumerate(var_9) :
						if var_4 in var_10 :
							var_9 [var_3] = (var_10 [0],)
							break
				yield var_9
