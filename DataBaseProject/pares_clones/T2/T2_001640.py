def Run(self) :
	self.time0 = time.clock()
	self.JobBeginning(self.duration)
	try :
		for count in range(0, self.duration) :
			time.sleep(1.0)
			self.JobProgress(count)
			self.PossibleStoppingPoint()
	except InterruptedException :
		print("canceled prematurely!")
	self.JobFinished()


def var_1(var_2) :
	var_2.var_3 = var_4.var_5()
	var_2.var_6(var_2.var_7)
	try :
		for var_8 in range(0, var_2.var_7) :
			var_4.var_9(1.0)
			var_2.var_10(var_8)
			var_2.var_11()
	except var_12 :
		print("canceled prematurely!")
	var_2.var_13()
