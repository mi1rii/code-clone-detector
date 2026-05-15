def seq(start, end, step) :
	if step == 0 :
		raise ValueError("step must not be 0")
	sample_count = int(abs(end - start) / step)
	return itertools.islice(itertools.count(start, step), sample_count)


def var_1(var_2, var_3, var_4) :
	if var_4 == 0 :
		raise var_5("step must not be 0")
	var_6 = int(abs(var_3 - var_2) / var_4)
	return var_7.var_8(var_7.var_9(var_2, var_4), var_6)
