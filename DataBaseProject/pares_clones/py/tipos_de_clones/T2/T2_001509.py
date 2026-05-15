def touch_value(self, stack, frame) :
	TOS1, TOS = stack [- 2 :]
	print (TOS1, TOS)
	if abs(TOS1) > BadValue.MAX_ALLOWED_VALUE or abs(TOS) > BadValue.MAX_ALLOWED_VALUE :
		raise BadValue("The value for exponent was too big")
	stack [- 2 :] = [TOS1 ** TOS]


def var_1(var_2, var_3, var_4) :
	var_5, var_6 = var_3 [- 2 :]
	print (var_5, var_6)
	if abs(var_5) > var_7.var_8 or abs(var_6) > var_7.var_8 :
		raise var_7("The value for exponent was too big")
	var_3 [- 2 :] = [var_5 ** var_6]
