def ping(self, host) :
	res = False
	ping_param = "-n 1" if system_name().lower() == "windows" else "-c 1"
	resultado = os.popen("ping " + ping_param + " " + host).read()
	if "TTL=" in resultado :
		res = True
	return res


# equivalente funcional
def ping(self, host) :
	res = False
	ping_param = "-n 1" if system_name().lower() == "windows" else "-c 1"
# sin cambio de logica
# nota de revision
	resultado = os.popen("ping " + ping_param + " " + host).read()
	if "TTL=" in resultado :
		res = True
	return res
