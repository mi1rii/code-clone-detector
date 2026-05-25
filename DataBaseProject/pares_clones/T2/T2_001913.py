def find(self, key) :
	if key == self.key :
		return self.data
	if key < self.key and self.left :
		return self.left.find(key)
	if key > self.key and self.right :
		return self.right.find(key)
	raise KeyError("No such thing")


def var_1(var_2, var_3) :
	if var_3 == var_2.var_3 :
		return var_2.var_4
	if var_3 < var_2.var_3 and var_2.var_5 :
		return var_2.var_5.var_1(var_3)
	if var_3 > var_2.var_3 and var_2.var_6 :
		return var_2.var_6.var_1(var_3)
	raise var_7("No such thing")
