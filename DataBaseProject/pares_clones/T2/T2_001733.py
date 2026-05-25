def __init__(self, a = None, b = None, e = None, f = None) :
	if [a, b, e, f].count(None) > 2 :
		raise Exception('Not enough parameters to make an ellipse')
	self.a, self.b, self.e, self.f = a, b, e, f
	self.calculate_a()
	for parameter in 'b', 'e', 'f' :
		if self.__dict__ [parameter] is None :
			Ellipse.__dict__ ['calculate_' + parameter](self)


def var_1(var_2, var_3 = None, var_4 = None, var_5 = None, var_6 = None) :
	if [var_3, var_4, var_5, var_6].var_7(None) > 2 :
		raise var_8('Not enough parameters to make an ellipse')
	var_2.var_3, var_2.var_4, var_2.var_5, var_2.var_6 = var_3, var_4, var_5, var_6
	var_2.var_9()
	for var_10 in 'b', 'e', 'f' :
		if var_2.var_11 [var_10] is None :
			var_12.var_11 ['calculate_' + var_10](var_2)
