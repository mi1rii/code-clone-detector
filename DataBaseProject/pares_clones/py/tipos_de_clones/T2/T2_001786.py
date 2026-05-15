def __call__(self, file) :
	hash = self.algorithm()
	with open(file, 'rb') as f :
		for chunk in iter(lambda : f.read(4096), '') :
			hash.update(chunk)
	return hash.hexdigest()


def var_1(var_2, var_3) :
	var_4 = var_2.var_5()
	with var_6(var_3, 'rb') as var_7 :
		for var_8 in var_9(lambda : var_7.var_10(4096), '') :
			var_4.var_11(var_8)
	return var_4.var_12()
