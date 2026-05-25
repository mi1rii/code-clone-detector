def __init__(self) :
	super(Dialog, self).__init__()
	layoutMain = QtGui.QVBoxLayout(self)
	listWidget = QtGui.QListWidget(self)
	gripper = QtGui.QSizeGrip(listWidget)
	l = QtGui.QHBoxLayout(listWidget)
	l.setContentsMargins(0, 0, 0, 0)
	l.addWidget(gripper, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
	layoutMain.addWidget(listWidget)
	layoutMain.addWidget(QtGui.QLabel("Test", self))
	self.setGeometry(200, 500, 200, 500)


def var_1(var_2) :
	var_3(var_4, var_2).var_1()
	var_5 = var_6.var_7(var_2)
	var_8 = var_6.var_9(var_2)
	var_10 = var_6.var_11(var_8)
	var_12 = var_6.var_13(var_8)
	var_12.var_14(0, 0, 0, 0)
	var_12.var_15(var_10, 0, var_16.var_17.var_18 | var_16.var_17.var_19)
	var_5.var_15(var_8)
	var_5.var_15(var_6.var_20("Test", var_2))
	var_2.var_21(200, 500, 200, 500)
