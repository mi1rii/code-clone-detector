def awesome(my_string) :
	if is_substr(my_string, ["A", "B", "C"]) :
		x = do_something() + complicated_thing()
	elif is_substr(my_string, ["1", "2", "3"]) :
		x = do_something_else() + complicated_thing()
	elif is_substr(my_string, ["!", "#", "$"]) :
		x = do_another_thing() + complicated_thing()
	return x + ("Hello" if some_condition(x) else "World")


def var_1(var_2) :
	if var_3(var_2, ["A", "B", "C"]) :
		var_4 = var_5() + var_6()
	elif var_3(var_2, ["1", "2", "3"]) :
		var_4 = var_7() + var_6()
	elif var_3(var_2, ["!", "#", "$"]) :
		var_4 = var_8() + var_6()
	return var_4 + ("Hello" if var_9(var_4) else "World")
