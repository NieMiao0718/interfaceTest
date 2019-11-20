import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import readExcel
from common.login import rq_data
from common.Print import log_print
import warnings

url = geturlParams.geturlParams().get_Url('tembin')# 调用我们的geturlParams获取我们拼接的URL
TestGet_xls = readExcel.readExcel().get_xls('test_get.xlsx', 'TestGet')

@paramunittest.parametrized(*TestGet_xls)
class testTestGet(unittest.TestCase):
    def setParameters(self, case_name, path, data, method, note):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.note = str(note)

    def setUp(self):
        print(self.case_name + ":", self.note + "\n" + "**********测试开始**********")

    def testcase(self):
        self.checkResult()

    def tearDown(self):
        print("**********测试结束，输出log完结**********\n")

    def checkResult(self):
        #替换请求值
        warnings.filterwarnings("ignore")
        real_url = url + self.path + self.data
        headers, cookies = rq_data()
        response = RunMain().run_main(self.method, real_url, headers=headers, cookies=cookies)

        #打印log
        log_print(self.method, real_url, response)

        #断言
        response = json.loads(response)# 将响应转换为字典格式
        if self.case_name == 'get_order_details':# 如果case_name是login，说明合法，返回的code应该为2000
            self.assertEqual(response['status'], 2000)
        if self.case_name == 'get_customer_details':
            self.assertEqual(response['status'], 2000)

if __name__ == '__main__':
    self.checkResult()
