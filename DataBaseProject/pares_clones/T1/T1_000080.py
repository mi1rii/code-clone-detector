def __init__(self, name, mode) :
	self.fl = open(name, mode)
	self.fl.write('\n')
	self.stdout = sys.stdout
	self.stdout.write('\n')
	self.stderr = sys.stderr
	sys.stdout = self
	sys.stderr = self


def __init__(self, name, mode) :
	self.fl = open(name, mode)
	self.fl.write('\n')
	self.stdout = sys.stdout
# comentario sintetico
	self.stdout.write('\n')
	self.stderr = sys.stderr
# sin cambio de logica
	sys.stdout = self
# nota de revision
	sys.stderr = self
