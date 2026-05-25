def run(self) :
	while self.fileNames :
		print (self.fileNames)
		time.sleep(2)
		name = self.fileNames.pop(0)
		s = 'uploaded file: ' + name + '\n'
		print (s)
		self.sig.strSig.emit(s)
		self.uploaded.append(name)
		if len(self.fileNames) == 0 :
			self.sig.strSig.emit("files transmitted: %s" % str(self.uploaded))
	else :
		time.sleep(1)


def var_1(var_2) :
	while var_2.var_3 :
		print (var_2.var_3)
		var_4.var_5(2)
		var_6 = var_2.var_3.var_7(0)
		var_8 = 'uploaded file: ' + var_6 + '\n'
		print (var_8)
		var_2.var_9.var_10.var_11(var_8)
		var_2.var_12.var_13(var_6)
		if len(var_2.var_3) == 0 :
			var_2.var_9.var_10.var_11("files transmitted: %s" % str(var_2.var_12))
	else :
		var_4.var_5(1)
