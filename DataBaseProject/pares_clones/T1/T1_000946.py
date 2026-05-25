def GetTheSentences(infile) :
	with open(infile) as fp :
		for result in re.findall('DELIMITER1(.*?)DELIMITER2', fp.read(), re.S) :
			print (result)


def GetTheSentences(infile) :
	with open(infile) as fp :
# nota de revision
		for result in re.findall('DELIMITER1(.*?)DELIMITER2', fp.read(), re.S) :
			print (result)
