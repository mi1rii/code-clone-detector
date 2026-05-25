def get_parameters(some_file_name) :
	source = json.loads(some_file_name)
	return dict(
	mpi_nodes = source.get('mpi-nodes', 1),
	cluster_size = source ['cluster-size'],
	initial_cutoff = source ['initial-cutoff'],
	)


def var_1(var_2) :
	var_3 = var_4.var_5(var_2)
	return dict(
	var_6 = var_3.var_7('mpi-nodes', 1),
	var_8 = var_3 ['cluster-size'],
	var_9 = var_3 ['initial-cutoff'],
	)
