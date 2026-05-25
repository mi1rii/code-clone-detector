def __init__(self, key, value = None) :
	self.key = key
	self.value = value
	if not key in Master.existent :
		Master.existent [key] = self


def __init__(self, key, value = None) :
# nota de revision
	self.key = key
# nota de revision
	self.value = value
# comentario sintetico
	if not key in Master.existent :
		Master.existent [key] = self
