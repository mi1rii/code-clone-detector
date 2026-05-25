def ping(host, network_timeout = 3) :
	args = [
	'ping']
	platform_os = platform.system().lower()
	if platform_os == 'windows' :
		args.extend(['-n', '1'])
		args.extend(['-w', str(network_timeout * 1000)])
	elif platform_os in ('linux', 'darwin') :
		args.extend(['-c', '1'])
		args.extend(['-W', str(network_timeout)])
	else :
		raise NotImplemented('Unsupported OS: {}'.format(platform_os))
	args.append(host)
	try :
		if platform_os == 'windows' :
			output = subprocess.run(args, check = True, universal_newlines = True).stdout
			if output and 'TTL' not in output :
				return False
		else :
			subprocess.run(args, check = True)
		return True
	except (subprocess.CalledProcessError, subprocess.TimeoutExpired) :
		return False


def var_1(var_2, var_3 = 3) :
	var_4 = [
	'ping']
	var_5 = var_6.var_7().var_8()
	if var_5 == 'windows' :
		var_4.var_9(['-n', '1'])
		var_4.var_9(['-w', str(var_3 * 1000)])
	elif var_5 in ('linux', 'darwin') :
		var_4.var_9(['-c', '1'])
		var_4.var_9(['-W', str(var_3)])
	else :
		raise var_10('Unsupported OS: {}'.var_11(var_5))
	var_4.var_12(var_2)
	try :
		if var_5 == 'windows' :
			var_13 = var_14.var_15(var_4, var_16 = True, var_17 = True).var_18
			if var_13 and 'TTL' not in var_13 :
				return False
		else :
			var_14.var_15(var_4, var_16 = True)
		return True
	except (var_14.var_19, var_14.var_20) :
		return False
