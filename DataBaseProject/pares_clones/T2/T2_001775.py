def __init__(self, iterable = {}, ** kwargs) :
	super(StrictDict, self).__init__({})
	keys = set(iterable.keys()).union(set(kwargs.keys()))
	if not keys.issuperset(self.required) :
		msg = str(self.__class__.__name__) + " requires: " + str([str(key) for key in self.required])
		raise AttributeError(msg)
	if len(list(self.at_least_one_required)) and len(list(keys.intersection(self.at_least_one_required))) < 1 :
		msg = str(self.__class__.__name__) + " requires at least one: " + str([str(key) for key in self.at_least_one_required])
		raise AttributeError(msg)
	for key, val in iterable.iteritems() :
		self.__setitem__(key, val)
	for key, val in kwargs.iteritems() :
		self.__setitem__(key, val)


def var_1(var_2, var_3 = {}, ** var_4) :
	var_5(var_6, var_2).var_1({})
	var_7 = set(var_3.var_7()).var_8(set(var_4.var_7()))
	if not var_7.var_9(var_2.var_10) :
		var_11 = str(var_2.var_12.var_13) + " requires: " + str([str(var_14) for var_14 in var_2.var_10])
		raise var_15(var_11)
	if len(list(var_2.var_16)) and len(list(var_7.var_17(var_2.var_16))) < 1 :
		var_11 = str(var_2.var_12.var_13) + " requires at least one: " + str([str(var_14) for var_14 in var_2.var_16])
		raise var_15(var_11)
	for var_14, var_18 in var_3.var_19() :
		var_2.var_20(var_14, var_18)
	for var_14, var_18 in var_4.var_19() :
		var_2.var_20(var_14, var_18)
