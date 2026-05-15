def polyfit2d(x, y, f, deg) :
	from numpy.polynomial import polynomial
	import numpy as np
	x = np.asarray(x)
	y = np.asarray(y)
	f = np.asarray(f)
	deg = np.asarray(deg)
	vander = polynomial.polyvander2d(x, y, deg)
	vander = vander.reshape((- 1, vander.shape [- 1]))
	f = f.reshape((vander.shape [0],))
	c = np.linalg.lstsq(vander, f) [0]
	return c.reshape(deg + 1)


def var_1(var_2, var_3, var_4, var_5) :
	from var_6.var_7 import var_7
	import var_6 as var_8
	var_2 = var_8.var_9(var_2)
	var_3 = var_8.var_9(var_3)
	var_4 = var_8.var_9(var_4)
	var_5 = var_8.var_9(var_5)
	var_10 = var_7.var_11(var_2, var_3, var_5)
	var_10 = var_10.var_12((- 1, var_10.var_13 [- 1]))
	var_4 = var_4.var_12((var_10.var_13 [0],))
	var_14 = var_8.var_15.var_16(var_10, var_4) [0]
	return var_14.var_12(var_5 + 1)
