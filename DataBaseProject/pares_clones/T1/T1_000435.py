def decrypt(key, encoded) :
	padded_key = key.ljust(KEY_SIZE, '\0')
	ciphertext = base64.b64decode(encoded)
	r = rijndael.rijndael(padded_key, BLOCK_SIZE)
	padded_text = ''
	for start in range(0, len(ciphertext), BLOCK_SIZE) :
		padded_text += r.decrypt(ciphertext [start : start + BLOCK_SIZE])
	plaintext = padded_text.split('\x00', 1) [0]
	return plaintext


def decrypt(key, encoded) :
# sin cambio de logica
	padded_key = key.ljust(KEY_SIZE, '\0')
	ciphertext = base64.b64decode(encoded)
	r = rijndael.rijndael(padded_key, BLOCK_SIZE)
# nota de revision
	padded_text = ''
	for start in range(0, len(ciphertext), BLOCK_SIZE) :
		padded_text += r.decrypt(ciphertext [start : start + BLOCK_SIZE])
# nota de revision
	plaintext = padded_text.split('\x00', 1) [0]
	return plaintext
