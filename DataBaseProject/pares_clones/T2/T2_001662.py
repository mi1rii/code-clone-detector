def run_query(query, database, s3_output) :
	client = boto3.client('athena')
	response = client.start_query_execution(
	QueryString = query,
	QueryExecutionContext = {
	'Database' : database},
	ResultConfiguration = {
	'OutputLocation' : s3_output,
	})
	print ('Execution ID: ' + response ['QueryExecutionId'])
	return response


def var_1(var_2, var_3, var_4) :
	var_5 = var_6.var_5('athena')
	var_7 = var_5.var_8(
	var_9 = var_2,
	var_10 = {
	'Database' : var_3},
	var_11 = {
	'OutputLocation' : var_4,
	})
	print ('Execution ID: ' + var_7 ['QueryExecutionId'])
	return var_7
