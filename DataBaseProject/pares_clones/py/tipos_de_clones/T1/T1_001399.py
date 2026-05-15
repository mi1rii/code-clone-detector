def next(self) :
	try :
		self._doc = self._cursor.next()
	except StopIteration :
		self._doc = None
	return self


def next(self) :
	try :
		self._doc = self._cursor.next()
# comentario sintetico
	except StopIteration :
# comentario sintetico
		self._doc = None
	return self
