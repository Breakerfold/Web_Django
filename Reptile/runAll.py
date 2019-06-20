# import unittest
# import sys
# sys.path.append('..\testCase\\')
# from .testCase.test_Login import test_Login
#
# suite = unittest.TestSuite()
# suite.addTest(test_Login('test_login_success'))
# suite.addTest(test_Login('test_login_name_not_exists'))
# suite.addTest(test_Login('test_login_password_error'))

# 运行测试集
# unittest.TextTestRunner().run(suite)

import unittest
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./testCase/")

f = open("report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="Exam System",description="测试描述").run(suite)
# HTMLTestRunner(stream=f,title="Api Test",description="测试描述",runner="卡卡").run(suite)
f.close()