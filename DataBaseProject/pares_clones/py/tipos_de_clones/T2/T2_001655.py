def get_leaves(self, node) :
	kids = getchildren(node)
	for i in kids :
		if leafnode(i) :
			self.get_leaves(i)
		else :
			a = process_leaf(i)
			self.list_of_leaves.append(a)


def var_1(var_2, var_3) :
	var_4 = var_5(var_3)
	for var_6 in var_4 :
		if var_7(var_6) :
			var_2.var_1(var_6)
		else :
			var_8 = var_9(var_6)
			var_2.var_10.var_11(var_8)
