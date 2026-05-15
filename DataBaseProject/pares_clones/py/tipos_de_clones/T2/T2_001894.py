def __init__(self, t) :
	self.i = Tkinter.PhotoImage(width = 100, height = 100)
	colors = [[random.randint(0, 255) for i in range(0, 3)] for j in range(0, 10000)]
	row = 0; col = 0
	for color in colors :
		self.i.put('#%02x%02x%02x' % tuple(color), (row, col))
		col += 1
		if col == 100 :
			row += 1; col = 0
	c = Tkinter.Canvas(t, width = 100, height = 100); c.pack()
	c.create_image(0, 0, image = self.i, anchor = Tkinter.NW)


def var_1(var_2, var_3) :
	var_2.var_4 = var_5.var_6(var_7 = 100, var_8 = 100)
	var_9 = [[var_10.var_11(0, 255) for var_4 in range(0, 3)] for var_12 in range(0, 10000)]
	var_13 = 0; var_14 = 0
	for var_15 in var_9 :
		var_2.var_4.var_16('#%02x%02x%02x' % tuple(var_15), (var_13, var_14))
		var_14 += 1
		if var_14 == 100 :
			var_13 += 1; var_14 = 0
	var_17 = var_5.var_18(var_3, var_7 = 100, var_8 = 100); var_17.var_19()
	var_17.var_20(0, 0, var_21 = var_2.var_4, var_22 = var_5.var_23)
