def merge(left_side, right_side) :
	result = []
	while len(left_side) > 0 or len(right_side) > 0 :
		if len(left_side) > 0 and len(right_side) > 0 :
			if left_side [0] < = right_side [0] :
				result.append(left_side.pop(0))
			else :
				result.append(right_side.pop(0))
		elif len(left_side) > 0 :
			result.append(left_side.pop(0))
		elif len(right_side) > 0 :
			result.append(right_side.pop(0))
	return result


def var_1(var_2, var_3) :
	var_4 = []
	while len(var_2) > 0 or len(var_3) > 0 :
		if len(var_2) > 0 and len(var_3) > 0 :
			if var_2 [0] < = var_3 [0] :
				var_4.var_5(var_2.var_6(0))
			else :
				var_4.var_5(var_3.var_6(0))
		elif len(var_2) > 0 :
			var_4.var_5(var_2.var_6(0))
		elif len(var_3) > 0 :
			var_4.var_5(var_3.var_6(0))
	return var_4
