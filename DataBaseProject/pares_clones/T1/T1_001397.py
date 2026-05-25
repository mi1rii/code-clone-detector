def update_model(self, index) :
	parent = self.model.itemFromIndex(index)
	for text in ["children1", "children2", "children3"] :
		children = QtGui.QStandardItem("{}_{}".format(parent.text(), text))
		parent.appendRow(children)
	self.mytreeview.expand(index)


def update_model(self, index) :
	parent = self.model.itemFromIndex(index)
# comentario sintetico
# sin cambio de logica
# sin cambio de logica
	for text in ["children1", "children2", "children3"] :
		children = QtGui.QStandardItem("{}_{}".format(parent.text(), text))
		parent.appendRow(children)
	self.mytreeview.expand(index)
