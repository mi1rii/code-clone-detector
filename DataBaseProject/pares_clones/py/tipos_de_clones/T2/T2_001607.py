def merge_sort(arr) :
	if len(arr) < 2 :
		return arr
	half = len(arr) / / 2
	left = merge_sort(arr [: half])
	right = merge_sort(arr [half :])
	out = []
	li = ri = 0
	while True :
		if li > = len(left) :
			out.extend(right [ri :])
			break
		if ri > = len(right) :
			out.extend(left [li :])
			break
		if left [li] < right [ri] :
			out.append(left [li])
			li += 1
		else :
			out.append(right [ri])
			ri += 1
	return out


def var_1(var_2) :
	if len(var_2) < 2 :
		return var_2
	var_3 = len(var_2) / / 2
	var_4 = var_1(var_2 [: var_3])
	var_5 = var_1(var_2 [var_3 :])
	var_6 = []
	var_7 = var_8 = 0
	while True :
		if var_7 > = len(var_4) :
			var_6.var_9(var_5 [var_8 :])
			break
		if var_8 > = len(var_5) :
			var_6.var_9(var_4 [var_7 :])
			break
		if var_4 [var_7] < var_5 [var_8] :
			var_6.var_10(var_4 [var_7])
			var_7 += 1
		else :
			var_6.var_10(var_5 [var_8])
			var_8 += 1
	return var_6
