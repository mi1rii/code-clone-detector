def __init__(self, ev_list = None) :
	self._trigger = Event()
	if ev_list :
		self._t_list = [
		Thread(target = self._triggerer, args = (ev,)) for ev in ev_list
		]
	else :
		self._t_list = []


def var_1(var_2, var_3 = None) :
	var_2.var_4 = var_5()
	if var_3 :
		var_2.var_6 = [
		var_7(var_8 = var_2.var_9, var_10 = (var_11,)) for var_11 in var_3
		]
	else :
		var_2.var_6 = []
