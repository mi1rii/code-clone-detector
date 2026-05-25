def __init__(self) :
	wx.Frame.__init__(self, None, - 1, "Test", size = (500, 270))
	panel = wx.Panel(self, - 1)
	self.buttonStart = wx.Button(panel, - 1, label = "Start thread", pos = (0, 0))
	self.buttonChange = wx.Button(panel, - 1, label = "Change var", pos = (0, 30))
	panel.Bind(wx.EVT_BUTTON, self.startThread, id = self.buttonStart.GetId())
	panel.Bind(wx.EVT_BUTTON, self.changeVar, id = self.buttonChange.GetId())


def var_1(var_2) :
	var_3.var_4.var_1(var_2, None, - 1, "Test", var_5 = (500, 270))
	var_6 = var_3.var_7(var_2, - 1)
	var_2.var_8 = var_3.var_9(var_6, - 1, var_10 = "Start thread", var_11 = (0, 0))
	var_2.var_12 = var_3.var_9(var_6, - 1, var_10 = "Change var", var_11 = (0, 30))
	var_6.var_13(var_3.var_14, var_2.var_15, var_16 = var_2.var_8.var_17())
	var_6.var_13(var_3.var_14, var_2.var_18, var_16 = var_2.var_12.var_17())
