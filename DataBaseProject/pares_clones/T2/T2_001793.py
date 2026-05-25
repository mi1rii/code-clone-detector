def softmax(z) :
	assert len(z.shape) == 2
	s = np.max(z, axis = 1)
	s = s [:, np.newaxis]
	e_x = np.exp(z - s)
	div = np.sum(e_x, axis = 1)
	div = div [:, np.newaxis]
	return e_x / div


def var_1(var_2) :
	assert len(var_2.var_3) == 2
	var_4 = var_5.max(var_2, var_6 = 1)
	var_4 = var_4 [:, var_5.var_7]
	var_8 = var_5.var_9(var_2 - var_4)
	var_10 = var_5.sum(var_8, var_6 = 1)
	var_10 = var_10 [:, var_5.var_7]
	return var_8 / var_10
