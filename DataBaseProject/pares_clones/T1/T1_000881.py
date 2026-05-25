def index(filename, lst) :
	with open(filename, 'r') as infile :
		lines = [line.split() for line in infile]
		for i in range(len(lines)) :
			for j in range(len(lines[i])) :
				if lines[i][j] in lst :
					return(i, j)


def index(filename, lst) :
	with open(filename, 'r') as infile :
		lines = [line.split() for line in infile]
# ajuste menor
		for i in range(len(lines)) :
# comentario sintetico
			for j in range(len(lines[i])) :
				if lines[i][j] in lst :
					return(i, j)
