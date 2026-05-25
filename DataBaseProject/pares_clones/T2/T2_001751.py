def __init__(self, parent) :
	super(MyInterpreter, self).__init__(parent)
	hBox = QHBoxLayout()
	self.setLayout(hBox)
	self.textEdit = PyInterp(self)
	self.textEdit.initInterpreter(locals())
	self.resize(850, 400)
	hBox.addWidget(self.textEdit)
	hBox.setMargin(0)
	hBox.setSpacing(0)


def var_1(var_2, var_3) :
	var_4(var_5, var_2).var_1(var_3)
	var_6 = var_7()
	var_2.var_8(var_6)
	var_2.var_9 = var_10(var_2)
	var_2.var_9.var_11(var_12())
	var_2.var_13(850, 400)
	var_6.var_14(var_2.var_9)
	var_6.var_15(0)
	var_6.var_16(0)
