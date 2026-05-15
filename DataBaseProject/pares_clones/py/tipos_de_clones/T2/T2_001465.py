def __eq__(self, other) :
	if not isinstance(other, FrozenDict) :
		return dict(self.iteritems()) == other
	if len(self) ! = len(other) :
		return False
	for key, value in self.iteritems() :
		try :
			if value ! = other [key] :
				return False
		except KeyError :
			return False
	return True


def var_1(var_2, var_3) :
	if not isinstance(var_3, var_4) :
		return dict(var_2.var_5()) == var_3
	if len(var_2) ! = len(var_3) :
		return False
	for var_6, var_7 in var_2.var_5() :
		try :
			if var_7 ! = var_3 [var_6] :
				return False
		except var_8 :
			return False
	return True
