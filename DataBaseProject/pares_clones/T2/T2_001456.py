def __init__(self, obj) :
	if self.__wraps__ is None :
		raise TypeError("base class Wrapper may not be instantiated")
	elif isinstance(obj, self.__wraps__) :
		self._obj = obj
	else :
		raise ValueError("wrapped object must be of %s" % self.__wraps__)


def var_1(var_2, var_3) :
	if var_2.var_4 is None :
		raise var_5("base class Wrapper may not be instantiated")
	elif isinstance(var_3, var_2.var_4) :
		var_2.var_6 = var_3
	else :
		raise var_7("wrapped object must be of %s" % var_2.var_4)
