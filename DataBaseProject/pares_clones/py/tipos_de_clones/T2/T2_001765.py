def __str__(self) :
	if self.cards :
		rep = ""
		for card in self.cards :
			rep += str(card) + "\t"
	else :
		rep = "<empty>"
	return rep


def var_1(var_2) :
	if var_2.var_3 :
		var_4 = ""
		for var_5 in var_2.var_3 :
			var_4 += str(var_5) + "\t"
	else :
		var_4 = "<empty>"
	return var_4
