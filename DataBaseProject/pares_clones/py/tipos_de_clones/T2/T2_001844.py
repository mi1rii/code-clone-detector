def decrypt(key, encoded) :
	padded_key = key.ljust(KEY_SIZE, '\0')
	ciphertext = base64.b64decode(encoded)
	r = rijndael.rijndael(padded_key, BLOCK_SIZE)
	padded_text = ''
	for start in range(0, len(ciphertext), BLOCK_SIZE) :
		padded_text += r.decrypt(ciphertext [start : start + BLOCK_SIZE])
	plaintext = padded_text.split('\x00', 1) [0]
	return plaintext


def var_1(var_2, var_3) :
	var_4 = var_2.var_5(var_6, '\0')
	var_7 = var_8.var_9(var_3)
	var_10 = var_11.var_11(var_4, var_12)
	var_13 = ''
	for var_14 in range(0, len(var_7), var_12) :
		var_13 += var_10.var_1(var_7 [var_14 : var_14 + var_12])
	var_15 = var_13.var_16('\x00', 1) [0]
	return var_15
