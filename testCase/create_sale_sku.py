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
from common.Log import logger

url = geturlParams.geturlParams().get_Url('tembin')# 调用我们的geturlParams获取我们拼接的URL
CreateSaleSku_xls_sheets = readExcel.readExcel().get_sheet('haishen_create_sale_sku.xlsx')
CreateSaleSku_xls = []
for sheet in CreateSaleSku_xls_sheets:
    CreateSaleSku_xls.extend(readExcel.readExcel().get_xls('haishen_create_sale_sku.xlsx', sheet))

@paramunittest.parametrized(*CreateSaleSku_xls)
class testCreateSaleSku(unittest.TestCase):
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

    def checkResult(self):# 断言
        headers, cookies = rq_data()
        if self.case_name == 'get_service_sku_list':
            real_url = url + self.path + self.data
            real_data = None
            response = json.loads(RunMain().run_main(self.method, real_url, headers=headers, cookies=cookies))
            response = response["result"]["objects"][0]
            global service_sku_id, service_sku_status
            service_sku_id = response["service_sku_id"]
            service_sku_status = response["status"]
            response = json.dumps(response, sort_keys=True, indent=4, separators=(',', ':'))
        if self.case_name == 'create_sale_sku':
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 4))
            real_url = url + self.path
            real_data = json.loads(self.data)
            real_data["sku_id"] = 'auto_sale_sku' + '_' + ran_str
            real_data["sku_name"] = real_data["sku_id"]
            if service_sku_id and service_sku_status:
                real_data["service_sku_id"] = service_sku_id
            else:
                print("无上架的服务规格，请先创建服务规格！！！")
                logger.info("无上架的服务规格，请先创建服务规格！！！")
            response = RunMain().run_main(self.method, real_url, real_data, headers, cookies)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应

        # 打印log
        log_print(self.method, real_url, response, real_data)

        # 断言
        response = json.loads(response)# 将响应转换为字典格式
        if self.case_name == 'create_sale_sku':
            self.assertEqual(response['status'], 2000)

if __name__ == '__main__':
    self.checkResult()