def __init__(self, name, mode) :
	self.fl = open(name, mode)
	self.fl.write('\n')
	self.stdout = sys.stdout
	self.stdout.write('\n')
	self.stderr = sys.stderr
	sys.stdout = self
	sys.stderr = self


def var_1(var_2, var_3, var_4) :
	var_2.var_5 = var_6(var_3, var_4)
	var_2.var_5.var_7('\n')
	var_2.var_8 = var_9.var_8
	var_2.var_8.var_7('\n')
	var_2.var_10 = var_9.var_10
	var_9.var_8 = var_2
	var_9.var_10 = var_2
