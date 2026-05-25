def __new__(meta, name, bases, attrs) :
	nt = namedtuple(name, attrs.pop('fields'))
	struct = attrs.pop('struct')


# equivalente funcional
def __new__(meta, name, bases, attrs) :
	nt = namedtuple(name, attrs.pop('fields'))
# ajuste menor
	struct = attrs.pop('struct')
