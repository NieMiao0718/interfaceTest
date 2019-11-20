import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import readExcel
import random
import string
from common.login import rq_data
from common.Print import log_print
import warnings

url = geturlParams.geturlParams().get_Url('tembin')# 调用我们的geturlParams获取我们拼接的URL
CreateCustomer_xls = readExcel.readExcel().get_xls('higos_create_customer.xlsx', 'CreateCustomer')

@paramunittest.parametrized(*CreateCustomer_xls)
class testCreateCustomer(unittest.TestCase):
#class testUserLogin(unittest.TestCase):
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
        warnings.filterwarnings("ignore")#忽略warnings
        #替换请求值
        real_url = url + self.path
        headers, cookies = rq_data()
        real_data = json.loads(self.data)
        if self.case_name == 'create_customer':
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 4))
            real_data["customer_name"] = 'auto_test' + '_' + ran_str
            response = RunMain().run_main(self.method, real_url, real_data, headers, cookies)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        else:
            response = RunMain().run_main(self.method, real_url, real_data, headers, cookies)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应

        # 打印log
        log_print(self.method, real_url, response, real_data)

        #断言
        response = json.loads(response)# 将响应转换为字典格式
        if self.case_name == 'create_customer':#
            self.assertEqual(response['status'], 2000)
        if self.case_name == 'create_customer_null':
            self.assertEqual(response['status'], 4000)
        if self.case_name == 'create_customer_dupl':
            self.assertEqual(response['status'], 4906)

if __name__ == '__main__':
    self.checkResult()