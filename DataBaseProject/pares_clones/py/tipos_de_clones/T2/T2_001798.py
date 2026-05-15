def test_func_happy_path(self, MockFTP, m_open) :
	MockFTP.return_value = Mock()
	mock_ftp_obj = MockFTP()
	m_open.return_value = Mock()
	func('localhost', 'fred', 's3Kr3t')
	assert mock_ftp_obj.retrbinary.called
	assert m_open.called
	m_open.assert_called_once_with('README', 'wb')


def var_1(var_2, var_3, var_4) :
	var_3.var_5 = var_6()
	var_7 = var_3()
	var_4.var_5 = var_6()
	var_8('localhost', 'fred', 's3Kr3t')
	assert var_7.var_9.var_10
	assert var_4.var_10
	var_4.var_11('README', 'wb')
