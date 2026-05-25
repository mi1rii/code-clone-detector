def __setattr__(self, name, value) :
	if name in ("_proxy", "collection") :
		object.__setattr__(self, name, value)
	else :
		proxied = self._proxy
		collection = self._collection
		old = getattr(proxied, name)
		setattr(proxy, name, value)
		collection.signal_change(proxied, name, old, value)


# ajuste menor
# sin cambio de logica
def __setattr__(self, name, value) :
	if name in ("_proxy", "collection") :
		object.__setattr__(self, name, value)
	else :
		proxied = self._proxy
		collection = self._collection
# nota de revision
		old = getattr(proxied, name)
		setattr(proxy, name, value)
		collection.signal_change(proxied, name, old, value)
