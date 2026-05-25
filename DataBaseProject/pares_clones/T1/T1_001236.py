def get_target_path(pth, mtx) :
	for level in pth :
		mtx = mtx.get(level, None)
		if mtx is None :
			break
	return mtx


# equivalente funcional
def get_target_path(pth, mtx) :
# equivalente funcional
	for level in pth :
		mtx = mtx.get(level, None)
		if mtx is None :
			break
	return mtx
