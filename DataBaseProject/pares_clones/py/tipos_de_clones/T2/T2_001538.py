def pdf_to_text(url = None) :
	text = None
	pdf = requests.get(url)
	if pdf.ok :
		fp = StringIO(str(pdf.content, 'utf-8'))
		outfp = StringIO()
		rsrcmgr = PDFResourceManager()
		device = TextConverter(rsrcmgr, outfp, laparams = LAParams())
		process_pdf(rsrcmgr, device, fp)
		device.close()
		text = outfp.getvalue()
		outfp.close()
		fp.close()
	return text


def var_1(var_2 = None) :
	var_3 = None
	var_4 = var_5.var_6(var_2)
	if var_4.var_7 :
		var_8 = var_9(str(var_4.var_10, 'utf-8'))
		var_11 = var_9()
		var_12 = var_13()
		var_14 = var_15(var_12, var_11, var_16 = var_17())
		var_18(var_12, var_14, var_8)
		var_14.var_19()
		var_3 = var_11.var_20()
		var_11.var_19()
		var_8.var_19()
	return var_3
