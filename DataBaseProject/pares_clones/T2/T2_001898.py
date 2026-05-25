def corr(data1, data2) :
	"data1 & data2 should be numpy arrays."
	mean1 = data1.mean()
	mean2 = data2.mean()
	std1 = data1.std()
	std2 = data2.std()
	corr = ((data1 * data2).mean() - mean1 * mean2) / (std1 * std2)
	return corr


def var_1(var_2, var_3) :
	"data1 & data2 should be numpy arrays."
	var_4 = var_2.var_5()
	var_6 = var_3.var_5()
	var_7 = var_2.var_8()
	var_9 = var_3.var_8()
	var_1 = ((var_2 * var_3).var_5() - var_4 * var_6) / (var_7 * var_9)
	return var_1
