def __init__(self, parent, this_worker) :
	self.parent = parent
	self.this_worker = this_worker
	QtGui.QTabWidget.__init__(self, parent)
	self.treeWidget = QtGui.QTreeWidget(self)
	self.properties = QtGui.QTreeWidgetItem(self.treeWidget, ["Properties"])
	self.step = QtGui.QTreeWidgetItem(self.properties, ["Iteration #"])
	self.thread = QtCore.QThread();
	self.this_worker.moveToThread(self.thread);
	self.this_worker.update_signal.connect(self.update_GUI)
	self.this_worker.done_signal.connect(self.thread.quit)
	self.start_comp.connect(self.this_worker.start_computation)
	self.thread.start()


def var_1(var_2, var_3, var_4) :
	var_2.var_3 = var_3
	var_2.var_4 = var_4
	var_5.var_6.var_1(var_2, var_3)
	var_2.var_7 = var_5.var_8(var_2)
	var_2.var_9 = var_5.var_10(var_2.var_7, ["Properties"])
	var_2.var_11 = var_5.var_10(var_2.var_9, ["Iteration #"])
	var_2.var_12 = var_13.var_14();
	var_2.var_4.var_15(var_2.var_12);
	var_2.var_4.var_16.var_17(var_2.var_18)
	var_2.var_4.var_19.var_17(var_2.var_12.var_20)
	var_2.var_21.var_17(var_2.var_4.var_22)
	var_2.var_12.var_23()
