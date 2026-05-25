def convert_pdf_to_txt(path, outtype = 'txt') :
	outfile = path [: - 3] + outtype
	rsrcmgr = PDFResourceManager()
	codec = 'utf-8'
	laparams = LAParams()
	if outfile :
		outfp = file(outfile, 'w')
	else :
		outfp = sys.stdout
	device = TextConverter(rsrcmgr, outfp, codec = codec, laparams = laparams)
	fp = file(path, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	password = ""
	maxpages = 0
	caching = True
	pagenos = set()
	for page in PDFPage.get_pages(fp, pagenos, maxpages = maxpages, password = password, caching = caching, check_extractable = True) :
		interpreter.process_page(page)
	fp.close()
	device.close()
	outfp.close()
	return


def var_1(var_2, var_3 = 'txt') :
	var_4 = var_2 [: - 3] + var_3
	var_5 = var_6()
	var_7 = 'utf-8'
	var_8 = var_9()
	if var_4 :
		var_10 = var_11(var_4, 'w')
	else :
		var_10 = var_12.var_13
	var_14 = var_15(var_5, var_10, var_7 = var_7, var_8 = var_8)
	var_16 = var_11(var_2, 'rb')
	var_17 = var_18(var_5, var_14)
	var_19 = ""
	var_20 = 0
	var_21 = True
	var_22 = set()
	for var_23 in var_24.var_25(var_16, var_22, var_20 = var_20, var_19 = var_19, var_21 = var_21, var_26 = True) :
		var_17.var_27(var_23)
	var_16.var_28()
	var_14.var_28()
	var_10.var_28()
	return
