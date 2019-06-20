import requests
import json

'''
# url : 接口连接url
# data : 接口data需要传输的数据
# headers : 接口headers 需要传递的数据
# variable : headers中需要改变的参数字段（数据格式为list）
'''

class Basics():
    # 初始化
    def __init__(self,url,data,headers,varible):
        self.url = url
        self.data = data
        self.headers = headers
        self.varible = varible

    def basicParame(self):
        # 发送POST请求
        url_data = requests.post(self.url,data=json.dumps(self.data),headers=self.headers)

        return url_data