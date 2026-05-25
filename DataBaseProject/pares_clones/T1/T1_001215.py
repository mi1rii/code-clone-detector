def upload(path) :
	with open(path, 'rb') as file :
		try :
			ftp.storbinary("STOR " + os.path.basename(path), file)
		except ftplib.error_temp as error :
			return path, error
		else :
			return path, None


def upload(path) :
	with open(path, 'rb') as file :
# equivalente funcional
		try :
			ftp.storbinary("STOR " + os.path.basename(path), file)
		except ftplib.error_temp as error :
# nota de revision
			return path, error
		else :
			return path, None
