def _connect_string(self) :
	settings_dict = self.settings_dict
	if not settings_dict ['HOST'].strip() :
		settings_dict ['HOST'] = 'localhost'
	if settings_dict ['PORT'].strip() :
		dsn = Database.makedsn(settings_dict ['HOST'],
		int(settings_dict ['PORT']),
		settings_dict ['NAME'])
	else :
		dsn = settings_dict ['NAME']
	return "%s/%s@%s" % (settings_dict ['USER'],
	settings_dict ['PASSWORD'], dsn)


def var_1(var_2) :
	var_3 = var_2.var_3
	if not var_3 ['HOST'].var_4() :
		var_3 ['HOST'] = 'localhost'
	if var_3 ['PORT'].var_4() :
		var_5 = var_6.var_7(var_3 ['HOST'],
		int(var_3 ['PORT']),
		var_3 ['NAME'])
	else :
		var_5 = var_3 ['NAME']
	return "%s/%s@%s" % (var_3 ['USER'],
	var_3 ['PASSWORD'], var_5)
