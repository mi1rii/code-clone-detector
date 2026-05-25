def checksum(msg) :
	s = 0
	for i in range(0, len(msg), 2) :
		w = ord(msg [i]) + (ord(msg [i + 1]) < < 8)
		s = carry_around_add(s, w)
	return ~ s & 0xffff


def var_1(var_2) :
	var_3 = 0
	for var_4 in range(0, len(var_2), 2) :
		var_5 = var_6(var_2 [var_4]) + (var_6(var_2 [var_4 + 1]) < < 8)
		var_3 = var_7(var_3, var_5)
	return ~ var_3 & 0xffff
