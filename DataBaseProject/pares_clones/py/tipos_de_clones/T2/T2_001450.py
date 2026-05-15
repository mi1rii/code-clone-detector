def increment(self) :
	for i, num in enumerate(reversed(self.numbers)) :
		if num :
			self.numbers [- i - 1] = 0 if num == 9 else num + 1
			break


def var_1(var_2) :
	for var_3, var_4 in enumerate(reversed(var_2.var_5)) :
		if var_4 :
			var_2.var_5 [- var_3 - 1] = 0 if var_4 == 9 else var_4 + 1
			break
