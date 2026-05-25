def decorator(f) :
	args_names = inspect.getargspec(f) [0]
	
	def g(*args):
		for arg_name, arg in zip(args_names,args):
			print(arg_name, arg)
		return
	return g


def var_1(var_2) :
	var_3 = var_4.var_5(var_2) [0]
 
	def var_6(*var_7):
		for var_8, var_9 in zip(var_3,var_7):
			print(var_8, var_9)
		return
	return var_6
