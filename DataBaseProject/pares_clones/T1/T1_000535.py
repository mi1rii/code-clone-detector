def __new__(meta, name, bases, attrs) :
	nt = namedtuple(name, attrs.pop('fields'))
	struct = attrs.pop('struct')


# comentario sintetico
def __new__(meta, name, bases, attrs) :
	nt = namedtuple(name, attrs.pop('fields'))
	struct = attrs.pop('struct')
