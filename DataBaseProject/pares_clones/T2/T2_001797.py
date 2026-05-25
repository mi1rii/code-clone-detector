def __setattr__(self, name, value) :
	if name in ("_proxy", "collection") :
		object.__setattr__(self, name, value)
	else :
		proxied = self._proxy
		collection = self._collection
		old = getattr(proxied, name)
		setattr(proxy, name, value)
		collection.signal_change(proxied, name, old, value)


def var_1(var_2, var_3, var_4) :
	if var_3 in ("_proxy", "collection") :
		var_5.var_1(var_2, var_3, var_4)
	else :
		var_6 = var_2.var_7
		var_8 = var_2.var_9
		var_10 = var_11(var_6, var_3)
		var_12(var_13, var_3, var_4)
		var_8.var_14(var_6, var_3, var_10, var_4)
