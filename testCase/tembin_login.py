import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel
from common.login import rq_data

url = geturlParams.geturlParams().get_Url('tembin')# 调用我们的geturlParams获取我们拼接的URL
TembinLogin_xls = readExcel.readExcel().get_xls('tembin_login.xlsx', 'TembinLogin')
#print(CreateCustomer_xls)

@paramunittest.parametrized(*TembinLogin_xls)
class testTembinLogin(unittest.TestCase):
#class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, data, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")

    #def create_customer(self):
    def testcase(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        #url1 = "http://www.xxx.com/login?"
        #new_url = url1 + self.query
        #data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))# 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        #real_url = url + '/api/nuri/higos/customer/'
        real_url = url + self.path
        headers, cookies = rq_data()
        response_data = RunMain().run_main(self.method, real_url, json.loads(self.data), headers, cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应

        response_data = json.loads(response_data)# 将响应转换为字典格式
        if self.case_name == 'tembin_login':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(response_data['status'], 2000)
            #print(response_data)
        if self.case_name == 'tembin_login_error':# 同上
            self.assertEqual(response_data['status'], 4034)

if __name__ == '__main__':
    self.checkResult()