def urls() :
	conn = sqlite3.connect('C:\Users\username\Desktop\History.sql')
	c = conn.cursor()
	query = "SELECT url, title FROM urls"
	c.execute(query)
	data = c.fetchall()
	if data :
		with open("C:\Users\username\Desktop\\historyulrs.csv", 'w') as outfile :
			writer = csv.writer(outfile)
			writer.writerow(['URL', 'Title'])
			for entry in data :
				writer.writerow([str(entry [0]), str(entry [1])])


def var_1() :
	var_2 = var_3.var_4('C:\Users\username\Desktop\History.sql')
	var_5 = var_2.var_6()
	var_7 = "SELECT url, title FROM urls"
	var_5.var_8(var_7)
	var_9 = var_5.var_10()
	if var_9 :
		with var_11("C:\Users\username\Desktop\\historyulrs.csv", 'w') as var_12 :
			var_13 = var_14.var_13(var_12)
			var_13.var_15(['URL', 'Title'])
			for var_16 in var_9 :
				var_13.var_15([str(var_16 [0]), str(var_16 [1])])
