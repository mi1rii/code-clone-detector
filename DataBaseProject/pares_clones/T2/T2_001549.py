def curry(f) :
	@ wraps(f)
	def cf(*x) :
		return f(*x) if len(x) == f.__code__.co_argcount else lambda *y : f(*x, *y)
	return cf


def var_1(var_2) :
	@ var_3(var_2)
	def var_4(*var_5) :
		return var_2(*var_5) if len(var_5) == var_2.var_6.var_7 else lambda *var_8 : var_2(*var_5, *var_8)
	return var_4
