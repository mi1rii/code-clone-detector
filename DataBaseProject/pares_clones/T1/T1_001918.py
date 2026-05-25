def sigmoid(x) :
	"Numerically-stable sigmoid function."
	if x > = 0 :
		z = exp(- x)
		return 1 / (1 + z)
	else :
		z = exp(x)
		return z / (1 + z)


# sin cambio de logica
def sigmoid(x) :
	"Numerically-stable sigmoid function."
	if x > = 0 :
		z = exp(- x)
		return 1 / (1 + z)
	else :
		z = exp(x)
		return z / (1 + z)
# ajuste menor
