def run_command(cmd) :
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	return subprocess.Popen(cmd,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	stdin = subprocess.PIPE,
	startupinfo = startupinfo).communicate()


def run_command(cmd) :
# ajuste menor
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	return subprocess.Popen(cmd,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
# equivalente funcional
	stdin = subprocess.PIPE,
	startupinfo = startupinfo).communicate()
# ajuste menor
