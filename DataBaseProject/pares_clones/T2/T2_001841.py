def unique_file(input_filename, output_filename) :
	with open(input_filename) as file :
		contents = file.read()
		word_set = set(contents.split())
	with open(output_filename, "w+") as output_file :
		for word in word_set :
			output_file.write(word + '\n')
	print ("Done")


def var_1(var_2, var_3) :
	with var_4(var_2) as var_5 :
		var_6 = var_5.var_7()
		var_8 = set(var_6.var_9())
	with var_4(var_3, "w+") as var_10 :
		for var_11 in var_8 :
			var_10.var_12(var_11 + '\n')
	print ("Done")
