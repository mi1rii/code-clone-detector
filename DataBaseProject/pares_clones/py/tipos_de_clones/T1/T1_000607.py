def __getattr__(self, key) :
	try :
		return wrap(getattr(self.obj, key))
	except AttributeError :
		try :
			return self [key]
		except KeyError :
			raise AttributeError(key)


def __getattr__(self, key) :
# comentario sintetico
	try :
		return wrap(getattr(self.obj, key))
	except AttributeError :
		try :
			return self [key]
# ajuste menor
		except KeyError :
			raise AttributeError(key)
# equivalente funcional
