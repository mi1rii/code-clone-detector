def main() :
	q = Queue()
	p1 = Process(target = f1, args = (q,))
	p1.start()
	p2 = Process(target = f2, args = (q,))
	p2.start()
	while True :
		try :
			print q.get()
		except :
			break


def var_1() :
	var_2 = var_3()
	var_4 = var_5(var_6 = var_7, var_8 = (var_2,))
	var_4.var_9()
	var_10 = var_5(var_6 = var_11, var_8 = (var_2,))
	var_10.var_9()
	while True :
		try :
			print var_2.var_12()
		except :
			break
