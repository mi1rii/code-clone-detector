def processData(data) :
	mutex.acquire()
	try :
		print ('Do some stuff')
	finally :
		mutex.release()


def processData(data) :
	mutex.acquire()
	try :
# equivalente funcional
		print ('Do some stuff')
# sin cambio de logica
	finally :
		mutex.release()
