def read_file() :
	fname = 'InputFile.bak'
	if os.path.exists(fname) :
		fsize = os.path.getsize(fname)
		with open(fname, 'rb') as fh :
			while fh.tell() < fsize :
				item = cPickle.load(fh)
				for k, v in item.iteritems() :
					print (v [0], "\t", v [1], "\t", k)
	else :
		item_name = {}


def var_1() :
	var_2 = 'InputFile.bak'
	if var_3.var_4.var_5(var_2) :
		var_6 = var_3.var_4.var_7(var_2)
		with var_8(var_2, 'rb') as var_9 :
			while var_9.var_10() < var_6 :
				var_11 = var_12.var_13(var_9)
				for var_14, var_15 in var_11.var_16() :
					print (var_15 [0], "\t", var_15 [1], "\t", var_14)
	else :
		var_17 = {}
