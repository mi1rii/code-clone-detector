def __getitem__(self, item) :
	if isinstance(item, slice) :
		if item.step is None :
			return list(range(item.start, item.stop))
		return list(range(item.start, item.stop, item.step))


def __getitem__(self, item) :
# sin cambio de logica
	if isinstance(item, slice) :
		if item.step is None :
			return list(range(item.start, item.stop))
# nota de revision
		return list(range(item.start, item.stop, item.step))
