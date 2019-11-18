import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
import random
import string
from common.login import rq_data
from common.Log import logger
# pythoncom.CoInitialize()

url = geturlParams.geturlParams().get_Url('tembin')# 调用我们的geturlParams获取我们拼接的URL
CreateSaleSku_xls_sheets = readExcel.readExcel().get_sheet('haishen_create_sale_sku.xlsx')
CreateSaleSku_xls = []
for sheet in CreateSaleSku_xls_sheets:
    CreateSaleSku_xls.extend(readExcel.readExcel().get_xls('haishen_create_sale_sku.xlsx', sheet))

@paramunittest.parametrized(*CreateSaleSku_xls)
class testCreateSaleSku(unittest.TestCase):
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
        if self.case_name == 'get_service_sku_list':
            url1 = url + self.path + self.data
            res1 = json.loads(RunMain().run_main(self.method, url1, headers=headers, cookies=cookies))
            global service_sku1_id, service_sku1_status
            service_sku1_id = res1["result"]["objects"][0]["service_sku_id"]
            service_sku1_status = res1["result"]["objects"][0]["status"]
            print(service_sku1_id)
        if self.case_name == 'create_sale_sku':
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 4))
            real_url = url + self.path
            real_data = json.loads(self.data)
            real_data["sku_id"] = 'auto_sale_sku' + '_' + ran_str
            real_data["sku_name"] = real_data["sku_id"]
            if service_sku1_id and service_sku1_status:
                real_data["service_sku_id"] = service_sku1_id
            else:
                print("无上架的服务规格，请先创建服务规格！！！")
                logger.info("无上架的服务规格，请先创建服务规格！！！")

            info = RunMain().run_main(self.method, real_url, real_data, headers, cookies)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应

            ss = json.loads(info)# 将响应转换为字典格式
            #if self.case_name == 'create_sale_sku':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['status'], 2000)
            print(ss)

if __name__ == '__main__':
    self.checkResult()