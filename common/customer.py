import json
import requests
import geturlParams
from common.login import rq_data

headers, cookies = rq_data()
def create_customer(name):
    url = geturlParams.geturlParams().get_Url('tembin') + "/api/tembin/higos/customer/"
    data = {"customer_name": name}
    res = requests.post(url=url, json=data, headers=headers, cookies=cookies, verify=False)
    res = res.json()
    customer_id = res["result"]["customer_id"]
    return customer_id

def acct_data(name):
    url = geturlParams.geturlParams().get_Url('tembin') + "/api/tembin/higos/customers/?customer_name=" + name
    res = requests.get(url=url, headers=headers, cookies=cookies, verify=False)
    res = res.json()
    res = res["result"]["objects"]
    if res:
        customer_id = res[0]["customer_id"]
        #print("aaaaaaaaaaaaaaaaaaaaaaaaa")
        return customer_id
    else:
        customer_id = create_customer(name)
        #print("bbbbbbbbbbbbbbbbbbbbbbbb")
        return customer_id

if __name__ == '__main__':
    cus_id = acct_data("test11146")
    print("sssssssss", cus_id)
