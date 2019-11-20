#!/usr/bin/python3

import os
import json
import getpathInfo#引入我们自己的写的获取路径的类
from readConfig import ReadConfig

readconfig = ReadConfig()

class geturlParams():# 定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self, url_type):
        url_config = readconfig.get_url()
        url_data = url_config[url_type]
        url = url_data["protocol"] + '://' + url_data["domain"] + ':' + url_data["port"]
        return url

if __name__ == '__main__':# 验证拼接后的正确性
    print(geturlParams().get_Url('nuri'))
    print(geturlParams().get_Url('tembin'))

