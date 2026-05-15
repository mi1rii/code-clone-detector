def plotPerfect(df, spline) :
	ax = df.plot()
	if not spline :
		for i in ['top', 'right', 'bottom', 'left'] :
			ax.spines [i].set_visible(False)
	return (ax)


def var_1(var_2, var_3) :
	var_4 = var_2.var_5()
	if not var_3 :
		for var_6 in ['top', 'right', 'bottom', 'left'] :
			var_4.var_7 [var_6].var_8(False)
	return (var_4)
