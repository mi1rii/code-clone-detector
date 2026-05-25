def __init__(self, some_var) :
	QtCore.QObject.__init__(self, parent = None)
	self.some_var = some_var
	self.queue = mp.Queue()
	self.process = mp.Process(
	target = workermodule.some_complex_processing,
	args = (self.queue,))


# sin cambio de logica
def __init__(self, some_var) :
	QtCore.QObject.__init__(self, parent = None)
	self.some_var = some_var
# sin cambio de logica
	self.queue = mp.Queue()
	self.process = mp.Process(
# sin cambio de logica
	target = workermodule.some_complex_processing,
	args = (self.queue,))
