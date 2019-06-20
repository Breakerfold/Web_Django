import unittest
from HTMLTestReportCN import HtmlTestRunner

suite = unittest.defaultTestLoader.discover('./')

# 输出测试结果到文本文件中
with open('Result.html','w') as f:
    unittest.TextTestRunner().run(suite)    # 将输出流stream输出到文件