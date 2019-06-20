import sys
import unittest
import json
import requests
sys.path.append('..\public\\')
from public.readConfig import readConfig as cf
# from readConfig import readConfig as cf  # 文件本身执行时用此引包


class test_Login(unittest.TestCase):

    url = cf().get_http("HTTP")+"/auth/login"
    headers = {"Content-Type": "application/json"}
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 登录成功
    def test_login_success(self):
        data = {
            "name":"student",
            "password":"123456"
        }
        res =requests.post(url=self.url,headers=self.headers,data=json.dumps(data))
        self.assertEqual(res.status_code,200)
        self.assertIn('0',res.text)


    # 用户不存在
    def test_login_name_not_exists(self):
        data = {
            "name": "admin123",
            "password": "123456"
        }
        res = requests.post(url=self.url,headers=self.headers,data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertIn('用户不存在',res.text)

    def test_login_password_error(self):
        data = {
            "name": "student",
            "password": "1234567"
        }
        res = requests.post(url=self.url, headers=self.headers, data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertIn('密码错误', res.text)

if __name__ == '__main__':

    unittest.main()
