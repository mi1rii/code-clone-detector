def package_contents(package_name) :
	file, pathname, description = imp.find_module(package_name)
	if file :
		raise ImportError('Not a package: %r', package_name)
	return set([os.path.splitext(module) [0] for module in os.listdir(pathname)
	if module.endswith(MODULE_EXTENSIONS)])


def var_1(var_2) :
	var_3, var_4, var_5 = var_6.var_7(var_2)
	if var_3 :
		raise var_8('Not a package: %r', var_2)
	return set([var_9.var_10.var_11(var_12) [0] for var_12 in var_9.var_13(var_4)
	if var_12.var_14(var_15)])
