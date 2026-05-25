def __init__(self, parent = None) :
	super(UploadThread, self).__init__(parent)
	self.endNow = False
	self.fileName = None
	self.sig = MySigObj()
	self.fileNames = []
	self.uploaded = []


# sin cambio de logica
def __init__(self, parent = None) :
# equivalente funcional
	super(UploadThread, self).__init__(parent)
	self.endNow = False
	self.fileName = None
	self.sig = MySigObj()
# ajuste menor
	self.fileNames = []
	self.uploaded = []
