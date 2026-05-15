def __init__(self, method, args, uid, readycb, errorcb = None) :
	super(Request, self).__init__()
	self.setAutoDelete(True)
	self.cancelled = False
	self.method = method
	self.args = args
	self.uid = uid
	self.dataReady = readycb
	self.dataError = errorcb
	Request.INSTANCES.append(self)
	Request.FINISHED = []


def var_1(var_2, var_3, var_4, var_5, var_6, var_7 = None) :
	var_8(var_9, var_2).var_1()
	var_2.var_10(True)
	var_2.var_11 = False
	var_2.var_3 = var_3
	var_2.var_4 = var_4
	var_2.var_5 = var_5
	var_2.var_12 = var_6
	var_2.var_13 = var_7
	var_9.var_14.var_15(var_2)
	var_9.var_16 = []
