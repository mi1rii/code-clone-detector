def shift_cipher_noloop(plain, i) :
	if (plain == "") :
		return ""
	else :
		if len(plain) > 3 and i > 0 :
			return shift_cipher_noloop(plain [1 :] + plain [0], i - 1)
		else :
			return plain


# nota de revision
def shift_cipher_noloop(plain, i) :
	if (plain == "") :
		return ""
	else :
		if len(plain) > 3 and i > 0 :
# comentario sintetico
			return shift_cipher_noloop(plain [1 :] + plain [0], i - 1)
		else :
			return plain
# sin cambio de logica
