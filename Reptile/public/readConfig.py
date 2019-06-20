# -*- coding:utf-8
import os
import configparser

# 获取当前py文件地址
proDir = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
# 组合config文件地址
configPath = proDir + "\config\config.ini"
cf = configparser.ConfigParser()
cf.read(configPath,encoding='utf-8')

class readConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding='utf-8')

    # 获取http配置数据
    def get_http(self,name):
        addr = ''
        value = cf.options(name)
        for i in value:
            addr += cf.get(name,i)
            if i == 'method':
                addr += "://"
                continue
            if i == 'ip':
                addr += ":"
        return addr

    # 获取email配置数据
    def get_email(self,name):
        pass

    def get_db(self,name):
        pass

if __name__ == '__main__':
    print(readConfig().get_http("HTTP"))