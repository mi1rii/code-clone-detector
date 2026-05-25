def decorator(f) :
	@ wraps(f)
	def wrapper(*args , **kwargs) :
		# Before
		value = f(*args, **kwargs)
		# After
		return value
	return wrapper


def var_1(var_2) :
	@ var_3(var_2)
	def var_4(*var_5 , **var_6) :
	 # Before
		var_7 = var_2(*var_5, **var_6)
		# After
		return var_7
	return var_4
