def flatten(iterable) :
	iterator, sentinel, stack = iter(iterable), object(), []
	while True :
		value = next(iterator, sentinel)
		if value is sentinel :
			if not stack :
				break
			iterator = stack.pop()
		elif isinstance(value, str) :
			yield value
		else :
			try :
				new_iterator = iter(value)
			except TypeError :
				yield value
			else :
				stack.append(iterator)
				iterator = new_iterator


def var_1(var_2) :
	var_3, var_4, var_5 = var_6(var_2), var_7(), []
	while True :
		var_8 = var_9(var_3, var_4)
		if var_8 is var_4 :
			if not var_5 :
				break
			var_3 = var_5.var_10()
		elif isinstance(var_8, str) :
			yield var_8
		else :
			try :
				var_11 = var_6(var_8)
			except var_12 :
				yield var_8
			else :
				var_5.var_13(var_3)
				var_3 = var_11
