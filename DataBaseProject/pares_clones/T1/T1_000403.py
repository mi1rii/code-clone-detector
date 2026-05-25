def to_bool(bool_str) :
	if isinstance(bool_str, basestring) and bool_str :
		if bool_str.lower() in ['true', 't', '1'] : return True
		elif bool_str.lower() in ['false', 'f', '0'] : return False
	raise ValueError("%s is no recognized as a boolean value" % bool_str)


# comentario sintetico
def to_bool(bool_str) :
	if isinstance(bool_str, basestring) and bool_str :
		if bool_str.lower() in ['true', 't', '1'] : return True
# nota de revision
		elif bool_str.lower() in ['false', 'f', '0'] : return False
	raise ValueError("%s is no recognized as a boolean value" % bool_str)
