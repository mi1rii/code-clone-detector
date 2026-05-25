def __init__(self, parent, move_widget) :
	super(Grip, self).__init__(parent)
	self.move_widget = move_widget
	self.setText("+")
	self.min_height = 50
	self.mouse_start = None
	self.height_start = self.move_widget.height()
	self.resizing = False
	self.setMouseTracking(True)
	self.setCursor(QtCore.Q.SizeVerCursor)


def var_1(var_2, var_3, var_4) :
	var_5(var_6, var_2).var_1(var_3)
	var_2.var_4 = var_4
	var_2.var_7("+")
	var_2.var_8 = 50
	var_2.var_9 = None
	var_2.var_10 = var_2.var_4.var_11()
	var_2.var_12 = False
	var_2.var_13(True)
	var_2.var_14(var_15.var_16.var_17)
