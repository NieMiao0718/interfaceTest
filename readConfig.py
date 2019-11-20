import os
import configparser
import getpathInfo#引入我们自己的写的获取路径的类
import json

path = getpathInfo.get_Path()#调用实例化，还记得这个类返回的路径为C:\Users\songlihui\PycharmProjects\dkxinterfaceTest
config_path = os.path.join(path, 'config.json')#这句话是在path路径下再加一级，最后变成C:\Users\songlihui\PycharmProjects\dkxinterfaceTest\config.ini
f = open(config_path, 'r', encoding='utf-8')
config = json.load(f)
f.close()

class ReadConfig():

    def get_url(self):
        value = config["URL"]
        return value
    def get_mail(self):
        value = config["Mail"]
        return value
    def get_mysql(self, name):#写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    print('URL：', ReadConfig().get_url())
    print('EMAIL:', ReadConfig().get_mail())


