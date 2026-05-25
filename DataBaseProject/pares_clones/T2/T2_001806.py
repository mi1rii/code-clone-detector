def __init__(self) :
	super().__init__()
	self.label = QLabel("0")
	self.obj = worker.Worker()
	self.thread = QThread()
	self.obj.intReady.connect(self.onIntReady)
	self.obj.moveToThread(self.thread)
	self.obj.finished.connect(self.thread.quit)
	self.thread.started.connect(self.obj.procCounter)
	self.thread.start()
	self.initUI()


def var_1(var_2) :
	var_3().var_1()
	var_2.var_4 = var_5("0")
	var_2.var_6 = var_7.var_8()
	var_2.var_9 = var_10()
	var_2.var_6.var_11.var_12(var_2.var_13)
	var_2.var_6.var_14(var_2.var_9)
	var_2.var_6.var_15.var_12(var_2.var_9.var_16)
	var_2.var_9.var_17.var_12(var_2.var_6.var_18)
	var_2.var_9.var_19()
	var_2.var_20()
