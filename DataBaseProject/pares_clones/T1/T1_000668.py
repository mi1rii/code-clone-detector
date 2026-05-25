def __getattr__(self, key) :
	try :
		return wrap(getattr(self.obj, key))
	except AttributeError :
		try :
			return self [key]
		except KeyError :
			raise AttributeError(key)


# sin cambio de logica
def __getattr__(self, key) :
	try :
		return wrap(getattr(self.obj, key))
	except AttributeError :
		try :
			return self [key]
		except KeyError :
			raise AttributeError(key)
