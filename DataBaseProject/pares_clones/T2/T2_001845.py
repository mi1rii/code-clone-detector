def __init__(self, * args, ** kwargs) :
	super(MainFrame, self).__init__(None, * args, ** kwargs)
	self.Title = 'Basic wxPython module'
	self.SetMenuBar(MenuBar(self))
	self.ToolBar = MainToolbar(self)
	self.status_bar = StatusBar(self).status_bar
	self.Bind(wx.EVT_CLOSE, self.on_quit_click)
	panel = MainPanel(self)
	sizer = wx.BoxSizer()
	sizer.Add(panel)
	self.SetSizerAndFit(sizer)
	self.Centre()
	self.Show()


def var_1(var_2, * var_3, ** var_4) :
	var_5(var_6, var_2).var_1(None, * var_3, ** var_4)
	var_2.var_7 = 'Basic wxPython module'
	var_2.var_8(var_9(var_2))
	var_2.var_10 = var_11(var_2)
	var_2.var_12 = var_13(var_2).var_12
	var_2.var_14(var_15.var_16, var_2.var_17)
	var_18 = var_19(var_2)
	var_20 = var_15.var_21()
	var_20.var_22(var_18)
	var_2.var_23(var_20)
	var_2.var_24()
	var_2.var_25()
