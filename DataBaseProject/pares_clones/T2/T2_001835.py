def window(seq, n = 2) :
	"Returns a sliding window (of width n) over data from the iterable"
	"   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
	it = iter(seq)
	result = tuple(islice(it, n))
	if len(result) == n :
		yield result
	for elem in it :
		result = result [1 :] + (elem,)
		yield result


def var_1(var_2, var_3 = 2) :
	"Returns a sliding window (of width n) over data from the iterable"
	"   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
	var_4 = var_5(var_2)
	var_6 = tuple(var_7(var_4, var_3))
	if len(var_6) == var_3 :
		yield var_6
	for var_8 in var_4 :
		var_6 = var_6 [1 :] + (var_8,)
		yield var_6
