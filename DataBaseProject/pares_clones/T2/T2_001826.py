def moto_boto() :
	mock_s3().start()
	res = boto3.resource('s3')
	res.create_bucket(Bucket = BUCKET)
	yield
	mock_s3.stop()


def var_1() :
	var_2().var_3()
	var_4 = var_5.var_6('s3')
	var_4.var_7(var_8 = var_9)
	yield
	var_2.var_10()
