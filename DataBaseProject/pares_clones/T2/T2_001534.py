def __init__(self, parent) :
	wx.Panel.__init__(self, parent)
	self.figure = mplFigure(figsize = (9, 6))
	self.ax = self.figure.add_subplot(111)
	self.ax.plot([1, 2, 3, 4], [2, 3, 5, 8], marker = "o", markersize = 20, picker = 10, linestyle = "None")
	self.canvas = mplCanvas(self, - 1, self.figure)
	self.figure.canvas.mpl_connect('pick_event', self.onClick)
	self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_down)
	self.canvas.Bind(wx.EVT_KEY_UP, self._on_key_up)
	self.states = {"cmd" : False, "ctrl" : False, "shift" : False}


def var_1(var_2, var_3) :
	var_4.var_5.var_1(var_2, var_3)
	var_2.var_6 = var_7(var_8 = (9, 6))
	var_2.var_9 = var_2.var_6.var_10(111)
	var_2.var_9.var_11([1, 2, 3, 4], [2, 3, 5, 8], var_12 = "o", var_13 = 20, var_14 = 10, var_15 = "None")
	var_2.var_16 = var_17(var_2, - 1, var_2.var_6)
	var_2.var_6.var_16.var_18('pick_event', var_2.var_19)
	var_2.var_16.var_20(var_4.var_21, var_2.var_22)
	var_2.var_16.var_20(var_4.var_23, var_2.var_24)
	var_2.var_25 = {"cmd" : False, "ctrl" : False, "shift" : False}
