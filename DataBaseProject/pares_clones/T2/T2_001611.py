def iter_n(self) :
	self.a, self.b = self.b, self.a + self.b
	if self.a > 10 :
		raise StopIteration();
	return self.a


def var_1(var_2) :
	var_2.var_3, var_2.var_4 = var_2.var_4, var_2.var_3 + var_2.var_4
	if var_2.var_3 > 10 :
		raise var_5();
	return var_2.var_3
