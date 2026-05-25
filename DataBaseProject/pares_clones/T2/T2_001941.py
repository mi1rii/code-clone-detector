def __init__(self) :
	super(Dialog, self).__init__()
	layout = QtGui.QVBoxLayout(self)
	splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
	layout.addWidget(splitter)
	list_widget = QtGui.QListWidget()
	splitter.addWidget(list_widget)
	splitter.addWidget(QtGui.QLabel("Test"))


def var_1(var_2) :
	var_3(var_4, var_2).var_1()
	var_5 = var_6.var_7(var_2)
	var_8 = var_6.var_9(var_10.var_11.var_12)
	var_5.var_13(var_8)
	var_14 = var_6.var_15()
	var_8.var_13(var_14)
	var_8.var_13(var_6.var_16("Test"))
