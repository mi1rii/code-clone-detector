def __call__(self, parser, namespace, values, option_string = None) :
	for value in values :
		try :
			n, v = value.split('=')
			setattr(namespace, n, v)
		except ValueError :
			setattr(namespace, '_unrecognized_args', values [values.index(value) :])


def var_1(var_2, var_3, var_4, var_5, var_6 = None) :
	for var_7 in var_5 :
		try :
			var_8, var_9 = var_7.var_10('=')
			var_11(var_4, var_8, var_9)
		except var_12 :
			var_11(var_4, '_unrecognized_args', var_5 [var_5.var_13(var_7) :])
