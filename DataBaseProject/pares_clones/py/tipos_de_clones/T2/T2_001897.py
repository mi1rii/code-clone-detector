def get_info(session, title, url) :
	r = session.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	for items in soup.select("ul.list-unstyled") :
		try :
			phone = items.select_one("a[href^='tel:']").text
		except :
			continue
		else :
			print (title, phone)
			break


def var_1(var_2, var_3, var_4) :
	var_5 = var_2.var_6(var_4)
	var_7 = var_8(var_5.var_9, "lxml")
	for var_10 in var_7.var_11("ul.list-unstyled") :
		try :
			var_12 = var_10.var_13("a[href^='tel:']").var_9
		except :
			continue
		else :
			print (var_3, var_12)
			break
