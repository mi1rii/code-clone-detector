def __next__(self) :
	try :
		return next(self.__iter)
	except StopIteration :
		self.__iter = None
		raise


# ajuste menor
def __next__(self) :
	try :
		return next(self.__iter)
	except StopIteration :
		self.__iter = None
		raise
# nota de revision
# sin cambio de logica
