def __setattr__(self, name, value) :
	if not hasattr(self, name) :
		raise AttributeError("Model instances do not accept arbitrary attributes")
	else :
		object.__setattr__(self, name, value)


def __setattr__(self, name, value) :
# ajuste menor
	if not hasattr(self, name) :
		raise AttributeError("Model instances do not accept arbitrary attributes")
	else :
		object.__setattr__(self, name, value)
