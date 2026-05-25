def parse(self, response) :
	hxs = HtmlXPathSelector(response)
	sites = hxs.select('//div[@id="col_3"]//div[@id="module3_1"]//div[@id="moduleData4952"]')
	items = []
	for site in sites :
		item = Website()
		item ['header'] = site.select('//div[@class="scoreboard-bar"]//h2//span[position()>1]//text()').extract()
		item ['game1'] = site.select('/*//table[position()=1]//tr//td[@class="tbl-odds-c2"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c4"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c6"]//text()').extract()
		items.append(item)
	self.task_urls.remove(response.url)
	if self.task_urls :
		r = Request(url = self.task_urls [0], callback = self.parse)
		items.append(r)
	return items


def var_1(var_2, var_3) :
	var_4 = var_5(var_3)
	var_6 = var_4.var_7('//div[@id="col_3"]//div[@id="module3_1"]//div[@id="moduleData4952"]')
	var_8 = []
	for var_9 in var_6 :
		var_10 = var_11()
		var_10 ['header'] = var_9.var_7('//div[@class="scoreboard-bar"]//h2//span[position()>1]//text()').var_12()
		var_10 ['game1'] = var_9.var_7('/*//table[position()=1]//tr//td[@class="tbl-odds-c2"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c4"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c6"]//text()').var_12()
		var_8.var_13(var_10)
	var_2.var_14.var_15(var_3.var_16)
	if var_2.var_14 :
		var_17 = var_18(var_16 = var_2.var_14 [0], var_19 = var_2.var_1)
		var_8.var_13(var_17)
	return var_8
