def __init__(self, * args, ** kwargs) :
	wx.Frame.__init__(self, * args, ** kwargs)
	self.panel = wx.Panel(self)
	self.button = wx.Button(self.panel, label = "Test")
	self.sizer = wx.BoxSizer()
	self.sizer.Add(self.button)
	self.panel.SetSizerAndFit(self.sizer)
	self.Show()


def var_1(var_2, * var_3, ** var_4) :
	var_5.var_6.var_1(var_2, * var_3, ** var_4)
	var_2.var_7 = var_5.var_8(var_2)
	var_2.var_9 = var_5.var_10(var_2.var_7, var_11 = "Test")
	var_2.var_12 = var_5.var_13()
	var_2.var_12.var_14(var_2.var_9)
	var_2.var_7.var_15(var_2.var_12)
	var_2.var_16()
