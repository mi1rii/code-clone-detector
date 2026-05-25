def search(self, st) :
	if self.value == st :
		return True
	for child in self.children :
		if child.search(st) :
			return True
	return False


def var_1(var_2, var_3) :
	if var_2.var_4 == var_3 :
		return True
	for var_5 in var_2.var_6 :
		if var_5.var_1(var_3) :
			return True
	return False
