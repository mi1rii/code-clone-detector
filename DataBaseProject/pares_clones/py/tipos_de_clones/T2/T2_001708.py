def test_run(files_dir) :
	queue = mp.Queue()
	procs = [mp.Process(target = worker, args = [queue]) for i in mp.cpu_count()]
	for p in procs :
		p.start()
	files = os.listdir(files_dir)
	for f1, f2 in IT.product(files, repeat = 2) :
		queue.put((f1, f2))
	for p in procs :
		queue.put(SENTINEL)
	for p in procs :
		p.join()


def var_1(var_2) :
	var_3 = var_4.var_5()
	var_6 = [var_4.var_7(var_8 = var_9, var_10 = [var_3]) for var_11 in var_4.var_12()]
	for var_13 in var_6 :
		var_13.var_14()
	var_15 = var_16.var_17(var_2)
	for var_18, var_19 in var_20.var_21(var_15, var_22 = 2) :
		var_3.var_23((var_18, var_19))
	for var_13 in var_6 :
		var_3.var_23(var_24)
	for var_13 in var_6 :
		var_13.var_25()
