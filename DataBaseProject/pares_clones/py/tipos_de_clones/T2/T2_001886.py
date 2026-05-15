def __call__(self, parser, args, values, option_string = None) :
	if values is None :
		self.values += 1
	else :
		try :
			self.values = int(values)
		except ValueError :
			self.values = values.count('v') + 1
	setattr(args, self.dest, self.values)


def var_1(var_2, var_3, var_4, var_5, var_6 = None) :
	if var_5 is None :
		var_2.var_5 += 1
	else :
		try :
			var_2.var_5 = int(var_5)
		except var_7 :
			var_2.var_5 = var_5.var_8('v') + 1
	var_9(var_4, var_2.var_10, var_2.var_5)
