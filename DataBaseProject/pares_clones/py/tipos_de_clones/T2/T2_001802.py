def singleton(class_) :
	class class_w(class_) :
		_instance = None
		def __new__(class_, *args, **kwargs) :
			if class_w._instance is None :
				class_w._instance = super().__new__(class_, *args, **kwargs)
			return class_w._instance


def var_1(var_2) :
	class var_3(var_2) :
		var_4 = None
		def var_5(var_2, *var_6, **var_7) :
			if var_3.var_4 is None :
				var_3.var_4 = var_8().var_5(var_2, *var_6, **var_7)
			return var_3.var_4
