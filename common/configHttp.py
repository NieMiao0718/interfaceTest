import requests
import json
from common.Log import logger
from common.login import rq_data
import warnings

logger = logger
class RunMain():
    def send_post(self, url, data, headers, cookies):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, json=data, headers=headers, cookies=cookies, verify=False)
        #response_headers = json.dumps(dict(result.headers), ensure_ascii=False, sort_keys=True, indent=2)
        response_data = json.dumps(result.json(), ensure_ascii=False, sort_keys=True, indent=2)
        return response_data

    def send_get(self, url, headers, cookies):
        result = requests.get(url=url, headers=headers, cookies=cookies, verify=False)
        response_data = json.dumps(result.json(), ensure_ascii=False, sort_keys=True, indent=2)
        return response_data

    def run_main(self, method, url, data=None, headers=None, cookies=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers, cookies)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, headers, cookies)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    #result = RunMain().run_main('post', 'http://127.0.0.1:8888/login?', 'name=xiaoming&pwd=111')
    warnings.filterwarnings("ignore")
    headers, cookies = rq_data()
    '''
    post_data = {"customer_name": "xiaomiing6"}
    post_result = RunMain().run_main('post', 'https://pre.sop.intra.nsfocus.com/api/tembin/higos/customer/', post_data, headers, cookies)
    print(post_result)
    '''
    get_data = "?order_id=1"
    url = 'https://pre.sop.intra.nsfocus.com/api/tembin/nangka/order_detail/' + get_data
    get_result = RunMain().run_main('get', url, headers=headers, cookies=cookies)
    print(get_result)
