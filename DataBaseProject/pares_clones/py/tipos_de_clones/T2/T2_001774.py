def __setattr__(self, key, value) :
	setIsOK = False
	for item in self.__List :
		if key == item :
			setIsOK = True
	if setIsOK == True :
		object.__setattr__(self, key, value)
	else :
		raise TypeError("%r has no attributes %r" % (self, key))


def var_1(var_2, var_3, var_4) :
	var_5 = False
	for var_6 in var_2.var_7 :
		if var_3 == var_6 :
			var_5 = True
	if var_5 == True :
		var_8.var_1(var_2, var_3, var_4)
	else :
		raise var_9("%r has no attributes %r" % (var_2, var_3))
