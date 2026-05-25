def decorator(f) :
	@ wraps(f)
	def wrapper(*args , **kwargs) :
		# Before
		value = f(*args, **kwargs)
		# After
		return value
	return wrapper


# sin cambio de logica
# equivalente funcional
def decorator(f) :
	@ wraps(f)
	def wrapper(*args , **kwargs) :
		# Before
		value = f(*args, **kwargs)
# equivalente funcional
		# After
		return value
	return wrapper
