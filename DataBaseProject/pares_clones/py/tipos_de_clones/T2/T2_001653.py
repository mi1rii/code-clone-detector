def get(self, request, * args, ** kwargs) :
	context = self.get_context_data()
	response = HttpResponse(content_type = 'application/pdf')
	response ['Content-Disposition'] = 'inline; filename="worksheet_pdf.pdf"'
	return response


def var_1(var_2, var_3, * var_4, ** var_5) :
	var_6 = var_2.var_7()
	var_8 = var_9(var_10 = 'application/pdf')
	var_8 ['Content-Disposition'] = 'inline; filename="worksheet_pdf.pdf"'
	return var_8
