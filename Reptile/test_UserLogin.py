# # -*- coding: utf-8 -*-
#
# import unittest
# import requests
# import json
#
# def setUpModule():         # 当前模块只执行一次
#     print(' ==== setUpModule ==== ')
#
# def rearDownModule():      # 当前模块只执行一次
#     print(' ==== rearDownModule ==== ')
#
# class test_User_Login_success(unittest.TestCase):
#
#     url = 'http://47.104.245.115:8080/Management-2.0.0/api/auth/login'
#
#     @classmethod  # 声明为类方法（必须）
#     def setUpClass(cls):  # 类方法，整个类只执行一次
#         print(' -------- setUpClass -------- ')
#
#     @classmethod  # 声明为类方法（必须）
#     def tearDownClass(cls):  # 类方法，整个类只执行一次
#         print(' -------- tearDownClass -------- ')
#
#     def setUp(self):
#         print('初始化数据中，请稍后....')
#         print(' .... setUp .... ')
#
#     def tearDown(self):
#         print(' .... tearDown .... ')
#         print('test_User_Login_success 类执行结束....')
#
#     def test_user_login_normal(self):
#         headers = {"Content-Type":"application/json"}
#         data = {
#             "name":"student",
#             "password":"123456"
#         }
#         res = requests.post(url=self.url,headers=headers,data=json.dumps(data))
#
#
#         self.assertIn('0', res.text)
#         # print(res.text)
#
#
#
# if __name__ == '__main__':
#     unittest.main()