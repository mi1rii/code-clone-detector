def __init__(self, some_var) :
	QtCore.QObject.__init__(self, parent = None)
	self.some_var = some_var
	self.queue = mp.Queue()
	self.process = mp.Process(
	target = workermodule.some_complex_processing,
	args = (self.queue,))


def var_1(var_2, var_3) :
	var_4.var_5.var_1(var_2, var_6 = None)
	var_2.var_3 = var_3
	var_2.var_7 = var_8.var_9()
	var_2.var_10 = var_8.var_11(
	var_12 = var_13.var_14,
	var_15 = (var_2.var_7,))
