def createfile() :
	var = """\
	#!/bin/sh
	echo ${test}
	"""
	var = textwrap.dedent(var)
	funcToCreateScript(filename, var)


def var_1() :
	var_2 = """\
	#!/bin/sh
	echo ${test}
	"""
	var_2 = var_3.var_4(var_2)
	var_5(var_6, var_2)
