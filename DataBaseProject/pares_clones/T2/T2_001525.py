def backupToZip(folder) :
	import zipfile, os
	folder = os.path.abspath(folder)
	for foldername, subfolders, filenames in os.walk(folder) :
		if foldername == folder :
			archive_folder_name = ''
		else :
			archive_folder_name = os.path.relpath(foldername, folder)
			backupZip.write(foldername, arcname = archive_folder_name)
		for filename in filenames :
			backupZip.write(os.path.join(foldername, filename), arcname = os.path.join(archive_folder_name, filename))
	backupZip.close()


def var_1(var_2) :
	import var_3, var_4
	var_2 = var_4.var_5.var_6(var_2)
	for var_7, var_8, var_9 in var_4.var_10(var_2) :
		if var_7 == var_2 :
			var_11 = ''
		else :
			var_11 = var_4.var_5.var_12(var_7, var_2)
			var_13.var_14(var_7, var_15 = var_11)
		for var_16 in var_9 :
			var_13.var_14(var_4.var_5.var_17(var_7, var_16), var_15 = var_4.var_5.var_17(var_11, var_16))
	var_13.var_18()
