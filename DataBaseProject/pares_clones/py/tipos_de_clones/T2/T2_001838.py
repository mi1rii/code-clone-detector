def find_nth(haystack, needle, n = 1) :
	if (hasattr(needle, 'finditer')) :
		matches = needle.finditer(haystack)
	else :
		matches = re.finditer(re.escape(needle), haystack)
	start_here = itertools.dropwhile(lambda x : x [0] < n, enumerate(matches, 1))
	try :
		return next(start_here) [1].start()
	except StopIteration :
		return - 1


def var_1(var_2, var_3, var_4 = 1) :
	if (var_5(var_3, 'finditer')) :
		var_6 = var_3.var_7(var_2)
	else :
		var_6 = var_8.var_7(var_8.var_9(var_3), var_2)
	var_10 = var_11.var_12(lambda var_13 : var_13 [0] < var_4, enumerate(var_6, 1))
	try :
		return var_14(var_10) [1].var_15()
	except var_16 :
		return - 1
