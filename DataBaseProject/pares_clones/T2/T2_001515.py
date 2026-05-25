def html_to_text(html) :
	"Creates a formatted text email message as a string from a rendered html template (page)"
	soup = BeautifulSoup(html, 'html.parser')
	body, text = soup.body, []
	for element in body.descendants :
		if type(element) == NavigableString :
			if element.parent.name in ('script', 'style') :
				continue
			string = ' '.join(element.string.split())
			if string :
				if element.parent.name == 'a' :
					a_tag = element.parent
					string = a_tag ['href']
					if (type(a_tag.previous_sibling) == NavigableString and
					a_tag.previous_sibling.string.strip()) :
						text [- 1] = text [- 1] + ' ' + string
						continue
				elif element.previous_sibling and element.previous_sibling.name == 'a' :
					text [- 1] = text [- 1] + ' ' + string
					continue
				elif element.parent.name == 'p' :
					string = '\n' + string
				text += [string]
	doc = '\n'.join(text)
	return doc


def var_1(var_2) :
	"Creates a formatted text email message as a string from a rendered html template (page)"
	var_3 = var_4(var_2, 'html.parser')
	var_5, var_6 = var_3.var_5, []
	for var_7 in var_5.var_8 :
		if var_9(var_7) == var_10 :
			if var_7.var_11.var_12 in ('script', 'style') :
				continue
			var_13 = ' '.var_14(var_7.var_13.var_15())
			if var_13 :
				if var_7.var_11.var_12 == 'a' :
					var_16 = var_7.var_11
					var_13 = var_16 ['href']
					if (var_9(var_16.var_17) == var_10 and
					var_16.var_17.var_13.var_18()) :
						var_6 [- 1] = var_6 [- 1] + ' ' + var_13
						continue
				elif var_7.var_17 and var_7.var_17.var_12 == 'a' :
					var_6 [- 1] = var_6 [- 1] + ' ' + var_13
					continue
				elif var_7.var_11.var_12 == 'p' :
					var_13 = '\n' + var_13
				var_6 += [var_13]
	var_19 = '\n'.var_14(var_6)
	return var_19
