def backspace(self) :
	self.current = self.current [0 : len(self.current) - 1]
	if self.current == "" :
		self.new_num = True
		self.current = "0"
	self.dsiplay(self.current)


def var_1(var_2) :
	var_2.var_3 = var_2.var_3 [0 : len(var_2.var_3) - 1]
	if var_2.var_3 == "" :
		var_2.var_4 = True
		var_2.var_3 = "0"
	var_2.var_5(var_2.var_3)
