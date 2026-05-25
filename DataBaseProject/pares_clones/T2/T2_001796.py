def __init__(self, widget) :
	logging.Handler.__init__(self)
	self.setLevel(logging.DEBUG)
	self.widget = widget
	self.widget.config(state = 'disabled')
	self.widget.tag_config("INFO", foreground = "black")
	self.widget.tag_config("DEBUG", foreground = "grey")
	self.widget.tag_config("WARNING", foreground = "orange")
	self.widget.tag_config("ERROR", foreground = "red")
	self.widget.tag_config("CRITICAL", foreground = "red", underline = 1)
	self.red = self.widget.tag_configure("red", foreground = "red")


def var_1(var_2, var_3) :
	var_4.var_5.var_1(var_2)
	var_2.var_6(var_4.var_7)
	var_2.var_3 = var_3
	var_2.var_3.var_8(var_9 = 'disabled')
	var_2.var_3.var_10("INFO", var_11 = "black")
	var_2.var_3.var_10("DEBUG", var_11 = "grey")
	var_2.var_3.var_10("WARNING", var_11 = "orange")
	var_2.var_3.var_10("ERROR", var_11 = "red")
	var_2.var_3.var_10("CRITICAL", var_11 = "red", var_12 = 1)
	var_2.var_13 = var_2.var_3.var_14("red", var_11 = "red")
