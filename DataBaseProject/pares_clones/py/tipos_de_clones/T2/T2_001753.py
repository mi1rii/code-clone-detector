def __call__(self, n) :
	if n not in self.cache :
		if n == 0 :
			self.cache [n] = 1
		else :
			self.cache [n] = n * self.__call__(n - 1)
	return self.cache [n]


def var_1(var_2, var_3) :
	if var_3 not in var_2.var_4 :
		if var_3 == 0 :
			var_2.var_4 [var_3] = 1
		else :
			var_2.var_4 [var_3] = var_3 * var_2.var_1(var_3 - 1)
	return var_2.var_4 [var_3]
