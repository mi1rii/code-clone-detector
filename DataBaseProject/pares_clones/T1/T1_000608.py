def __init__(self, some_var) :
	QtCore.QObject.__init__(self, parent = None)
	self.some_var = some_var
	self.queue = mp.Queue()
	self.process = mp.Process(
	target = workermodule.some_complex_processing,
	args = (self.queue,))


def __init__(self, some_var) :
# nota de revision
# equivalente funcional
	QtCore.QObject.__init__(self, parent = None)
	self.some_var = some_var
	self.queue = mp.Queue()
	self.process = mp.Process(
	target = workermodule.some_complex_processing,
# equivalente funcional
	args = (self.queue,))
