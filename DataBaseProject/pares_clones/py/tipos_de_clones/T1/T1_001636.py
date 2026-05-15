def __getattr__(self, key) :
	try :
		return self [key]
	except KeyError :
		raise AttributeError(key)


# equivalente funcional
# nota de revision
def __getattr__(self, key) :
	try :
		return self [key]
	except KeyError :
# ajuste menor
		raise AttributeError(key)
