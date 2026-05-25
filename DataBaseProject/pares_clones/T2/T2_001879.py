def __init__(self, maxlen, items = None) :
	self._maxlen = maxlen
	self.d = OrderedDict()
	if items :
		for k, v in items :
			self [k] = v


def var_1(var_2, var_3, var_4 = None) :
	var_2.var_5 = var_3
	var_2.var_6 = var_7()
	if var_4 :
		for var_8, var_9 in var_4 :
			var_2 [var_8] = var_9
