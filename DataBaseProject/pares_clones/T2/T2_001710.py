def __init__(self, a = None, b = None, ** kwargs) :
	self.relations = {
	"e" : {"req" : ["a", "b"], "func" : lambda a, b : a + b},
	"C" : {"req" : ["e", "a"], "func" : lambda e, a : e * 1 / (a * b)},
	"A" : {"req" : ["C", "e"], "func" : lambda e, C : cmplx_func_A(e, C)},
	"a" : {"req" : ["e", "b"], "func" : lambda e, b : e / b},
	"b" : {"req" : ["e", "a"], "func" : lambda e, a : e / a}}
	self.a = a
	self.b = b
	self.e = None
	self.C = None
	self.A = None
	if kwargs :
		for key in kwargs :
			setattr(self, key, kwargs [key])


def var_1(var_2, var_3 = None, var_4 = None, ** var_5) :
	var_2.var_6 = {
	"e" : {"req" : ["a", "b"], "func" : lambda var_3, var_4 : var_3 + var_4},
	"C" : {"req" : ["e", "a"], "func" : lambda var_7, var_3 : var_7 * 1 / (var_3 * var_4)},
	"A" : {"req" : ["C", "e"], "func" : lambda var_7, var_8 : var_9(var_7, var_8)},
	"a" : {"req" : ["e", "b"], "func" : lambda var_7, var_4 : var_7 / var_4},
	"b" : {"req" : ["e", "a"], "func" : lambda var_7, var_3 : var_7 / var_3}}
	var_2.var_3 = var_3
	var_2.var_4 = var_4
	var_2.var_7 = None
	var_2.var_8 = None
	var_2.var_10 = None
	if var_5 :
		for var_11 in var_5 :
			var_12(var_2, var_11, var_5 [var_11])
