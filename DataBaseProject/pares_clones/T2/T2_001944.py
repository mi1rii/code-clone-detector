def __new__(meta, name, bases, attrs) :
	nt = namedtuple(name, attrs.pop('fields'))
	struct = attrs.pop('struct')


def var_1(var_2, var_3, var_4, var_5) :
	var_6 = var_7(var_3, var_5.var_8('fields'))
	var_9 = var_5.var_8('struct')
