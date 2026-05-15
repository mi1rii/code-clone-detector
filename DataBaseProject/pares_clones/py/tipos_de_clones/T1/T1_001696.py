def __getitem__(self, key) :
	try :
		temp = int(key)
		return "I am a number"
	except ValueError :
		return self.get(key, None)


# equivalente funcional
def __getitem__(self, key) :
	try :
		temp = int(key)
# comentario sintetico
		return "I am a number"
	except ValueError :
		return self.get(key, None)
# ajuste menor
