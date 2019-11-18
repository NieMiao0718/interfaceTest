#!/usr/bin/python3

import os
import json
import getpathInfo#引入我们自己的写的获取路径的类

path = getpathInfo.get_Path()#调用实例化，还记得这个类返回的路径为C:\Users\songlihui\PycharmProjects\dkxinterfaceTest
config_path = os.path.join(path, 'config.json')#这句话是在path路径下再加一级，最后变成C:\Users\songlihui\PycharmProjects\dkxinterfaceTest\config.ini
f = open(config_path, 'r', encoding='utf-8')
config = json.load(f)
f.close()

class geturlParams():# 定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self, url_type):
        url_config = config["URL"]
        url_data = url_config[url_type]
        url = url_data["protocol"] + '://' + url_data["domain"] + ':' + url_data["port"]
        return url

if __name__ == '__main__':# 验证拼接后的正确性
    print(geturlParams().get_Url('nuri'))
    print(geturlParams().get_Url('tembin'))

