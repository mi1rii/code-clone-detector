def numpy_ewma(data, window) :
	returnArray = np.empty((data.shape [0]))
	returnArray.fill(np.nan)
	e = data [0]
	alpha = 2 / float(window + 1)
	for s in range(data.shape [0]) :
		e = ((data [s] - e) * alpha) + e
		returnArray [s] = e
	return returnArray


def var_1(var_2, var_3) :
	var_4 = var_5.var_6((var_2.var_7 [0]))
	var_4.var_8(var_5.var_9)
	var_10 = var_2 [0]
	var_11 = 2 / float(var_3 + 1)
	for var_12 in range(var_2.var_7 [0]) :
		var_10 = ((var_2 [var_12] - var_10) * var_11) + var_10
		var_4 [var_12] = var_10
	return var_4
