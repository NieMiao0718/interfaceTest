import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
from common.login import rq_data
from common.customer import acct_data
import datetime
# pythoncom.CoInitialize()

url = geturlParams.geturlParams().get_Url('tembin')# 调用我们的geturlParams获取我们拼接的URL
#create_formal_order_xls = readExcel.readExcel().get_xls('nangka_create_formal_order.xlsx', 'CreateFormalOrder_1101')
create_formal_order_xls_sheets = readExcel.readExcel().get_sheet('nangka_create_formal_order.xlsx')
create_formal_order_xls = []
for sheet in create_formal_order_xls_sheets:
    create_formal_order_xls.extend(readExcel.readExcel().get_xls('nangka_create_formal_order.xlsx', sheet))

@paramunittest.parametrized(*create_formal_order_xls)
class test_create_formal_order(unittest.TestCase):
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
        headers, cookies = rq_data()
        if self.case_name == 'get_sale_sku_list':
            url1 = url + self.path + self.data
            res1 = json.loads(RunMain().run_main(self.method, url1, headers=headers, cookies=cookies))
            global sale_sku_id, t_price, price_id
            sale_sku_id = res1["result"]["objects"][0]["sku_id"]
            t_price = res1["result"]["objects"][0]["c_price"][0]["t_price"]
            price_id = res1["result"]["objects"][0]["c_price"][0]["id"]
        if self.case_name == 'create_formal_order':
            real_url = url + self.path
            customer_id = acct_data("AutoTest_Nscloud")
            real_data = json.loads(self.data)
            real_data["customer_id"] = customer_id
            real_data["sku_id"] = sale_sku_id
            real_data["price"] = t_price
            real_data["price_id"] = price_id
            real_data["start_time"] = str(datetime.date.today())
            info = RunMain().run_main(self.method, real_url, real_data, headers, cookies)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应

            ss = json.loads(info)# 将响应转换为字典格式
            #if self.case_name == 'create_formal_order':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['status'], 2000)

if __name__ == '__main__':
    self.checkResult()