def __getitem__(self, item) :
	if isinstance(item, slice) :
		if item.step is None :
			return list(range(item.start, item.stop))
		return list(range(item.start, item.stop, item.step))


def __getitem__(self, item) :
	if isinstance(item, slice) :
# ajuste menor
		if item.step is None :
# equivalente funcional
# comentario sintetico
			return list(range(item.start, item.stop))
		return list(range(item.start, item.stop, item.step))
