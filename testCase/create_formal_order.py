import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import readExcel
from common.login import rq_data
from common.customer import acct_data
import datetime
from common.Print import log_print

url = geturlParams.geturlParams().get_Url('tembin')# 调用我们的geturlParams获取我们拼接的URL
create_formal_order_xls_sheets = readExcel.readExcel().get_sheet('nangka_create_formal_order.xlsx')
create_formal_order_xls = []
for sheet in create_formal_order_xls_sheets:
    create_formal_order_xls.extend(readExcel.readExcel().get_xls('nangka_create_formal_order.xlsx', sheet))

@paramunittest.parametrized(*create_formal_order_xls)
class test_create_formal_order(unittest.TestCase):
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
        headers, cookies = rq_data()
        if self.case_name == 'get_sale_sku_list':
            real_url = url + self.path + self.data
            real_data = None
            response = json.loads(RunMain().run_main(self.method, real_url, headers=headers, cookies=cookies))
            response = response["result"]["objects"][0]
            global sale_sku_id, t_price, price_id
            sale_sku_id = response["sku_id"]
            t_price = response["c_price"][0]["t_price"]
            price_id = response["c_price"][0]["id"]
            response = json.dumps(response, sort_keys=True, indent=4, separators=(',', ':'))
        if self.case_name == 'create_formal_order':
            real_url = url + self.path
            customer_id = acct_data("AutoTest_Nscloud")
            real_data = json.loads(self.data)
            real_data["customer_id"] = customer_id
            real_data["sku_id"] = sale_sku_id
            real_data["price"] = t_price
            real_data["price_id"] = price_id
            real_data["start_time"] = str(datetime.date.today())
            response = RunMain().run_main(self.method, real_url, real_data, headers, cookies)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应

        # 打印log
        log_print(self.method, real_url, response, real_data)

        # 断言
        response = json.loads(response)# 将响应转换为字典格式
        if self.case_name == 'create_formal_order':
            self.assertEqual(response['status'], 2000)

if __name__ == '__main__':
    self.checkResult()