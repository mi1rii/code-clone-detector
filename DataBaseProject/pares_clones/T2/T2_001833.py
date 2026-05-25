def __init__(self, key, value = None) :
	self.key = key
	self.value = value
	if not key in Master.existent :
		Master.existent [key] = self


def var_1(var_2, var_3, var_4 = None) :
	var_2.var_3 = var_3
	var_2.var_4 = var_4
	if not var_3 in var_5.var_6 :
		var_5.var_6 [var_3] = var_2
