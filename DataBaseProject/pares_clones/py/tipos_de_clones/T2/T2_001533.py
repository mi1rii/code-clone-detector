def onselect(evt) :
	w = evt.widget
	x = 0
	index = int(w.curselection() [0])
	value = w.get(index)
	print ('You selected item %d: "%s"' % (index, value))
	for y in enable :
		for item in list_for_listbox :
			globals() ["checkbox{}{}".format(item, y)].place_forget()
		globals() ["checkbox{}{}".format(value, y)].place(x = 300, y = 0 + x)
		x += 50


def var_1(var_2) :
	var_3 = var_2.var_4
	var_5 = 0
	var_6 = int(var_3.var_7() [0])
	var_8 = var_3.var_9(var_6)
	print ('You selected item %d: "%s"' % (var_6, var_8))
	for var_10 in var_11 :
		for var_12 in var_13 :
			var_14() ["checkbox{}{}".var_15(var_12, var_10)].var_16()
		var_14() ["checkbox{}{}".var_15(var_8, var_10)].var_17(var_5 = 300, var_10 = 0 + var_5)
		var_5 += 50
