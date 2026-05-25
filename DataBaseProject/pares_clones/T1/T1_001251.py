def formatTime(self, record, datefmt = None) :
	ct = self.converter(record.created)
	if datefmt :
		s = time.strftime(datefmt, ct)
	else :
		t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
		s = "%s.%03d" % (t, record.msecs)
	return s


# ajuste menor
def formatTime(self, record, datefmt = None) :
	ct = self.converter(record.created)
	if datefmt :
		s = time.strftime(datefmt, ct)
	else :
# ajuste menor
		t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
# ajuste menor
		s = "%s.%03d" % (t, record.msecs)
	return s
