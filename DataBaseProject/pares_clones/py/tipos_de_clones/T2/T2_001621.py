def run(self) :
	while True :
		log_level, message = self.queue.get()
		if log_level is None :
			self.log.info("Shutting down Central Logging process")
			break
		else :
			self.log.log(log_level, message)


def var_1(var_2) :
	while True :
		var_3, var_4 = var_2.var_5.var_6()
		if var_3 is None :
			var_2.var_7.var_8("Shutting down Central Logging process")
			break
		else :
			var_2.var_7.var_7(var_3, var_4)
