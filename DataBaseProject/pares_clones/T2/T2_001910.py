def write(self, data) :
	if data [0 : LOG_IDR_LENGTH] == LOG_IDENTIFIER :
		self.fl.write("%s\n" % data [LOG_IDR_LENGTH :])
		self.stdout.write(data [LOG_IDR_LENGTH :])
	else :
		timestamp = str(datetime.datetime.now())
		if 'Traceback' == data [0 : 9] :
			data = '%s: %s' % (timestamp, data)
			self.fl.write(data)
		else :
			self.fl.write(data)
		self.stdout.write(data)


def var_1(var_2, var_3) :
	if var_3 [0 : var_4] == var_5 :
		var_2.var_6.var_1("%s\n" % var_3 [var_4 :])
		var_2.var_7.var_1(var_3 [var_4 :])
	else :
		var_8 = str(var_9.var_9.var_10())
		if 'Traceback' == var_3 [0 : 9] :
			var_3 = '%s: %s' % (var_8, var_3)
			var_2.var_6.var_1(var_3)
		else :
			var_2.var_6.var_1(var_3)
		var_2.var_7.var_1(var_3)
