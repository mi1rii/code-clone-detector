def setup(self) :
	import os.path as op
	self.fixture_dir = op.join(op.abspath(op.dirname(__file__)), "fixtures")
	if not os.access(self.fixture_dir, os.F_OK) :
		raise AssertionError("Oops! "
		"the fixture dir should be here " + self.fixture_dir)
	csvfile = op.join(self.fixture_dir, "profiles-source1.csv")
	assert os.access(csvfile, os.F_OK)


def var_1(var_2) :
	import var_3.var_4 as var_5
	var_2.var_6 = var_5.var_7(var_5.var_8(var_5.var_9(var_10)), "fixtures")
	if not var_3.var_11(var_2.var_6, var_3.var_12) :
		raise var_13("Oops! "
		"the fixture dir should be here " + var_2.var_6)
	var_14 = var_5.var_7(var_2.var_6, "profiles-source1.csv")
	assert var_3.var_11(var_14, var_3.var_12)
