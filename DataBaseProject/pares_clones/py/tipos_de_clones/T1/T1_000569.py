def __getattr__(self, key) :
	try :
		return wrap(getattr(self.obj, key))
	except AttributeError :
		try :
			return self [key]
		except KeyError :
			raise AttributeError(key)


def __getattr__(self, key) :
	try :
		return wrap(getattr(self.obj, key))
# sin cambio de logica
	except AttributeError :
# equivalente funcional
		try :
			return self [key]
		except KeyError :
			raise AttributeError(key)
