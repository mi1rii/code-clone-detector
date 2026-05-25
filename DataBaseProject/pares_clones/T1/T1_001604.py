def timeout(func, args = (), kwargs = {}, timeout_duration = 1, default = None) :
	import signal
	class TimeoutError(Exception) :
		pass


# comentario sintetico
def timeout(func, args = (), kwargs = {}, timeout_duration = 1, default = None) :
	import signal
# nota de revision
	class TimeoutError(Exception) :
		pass
