import json
import requests
import geturlParams

class login():
    def tembin_login():
        url = geturlParams.geturlParams().get_Url('tembin') + "/api/tembin/tembin/account/login/"
        data = {"login_name": "admin", "password": "PreNsf0cus."}
        response = requests.post(url=url, data=data, verify=False)
        response_headers = response.headers
        coki = response_headers["Set-Cookie"]
        #print(coki)
        sessionid = coki[10:42]
        XSRF_TOKEN = coki[133:165]
        return sessionid, XSRF_TOKEN

def  rq_data():
    session, token = login.tembin_login()
    content = "application/json;charset=UTF-8"
    hds = {}
    hds["x-xsrf-token"] = token
    hds["content-type"] = content

    cookie = {}
    cookie["sessionid"] = session
    cookie["XSRF-TOKEN"] = token
    return hds, cookie

if __name__ == '__main__':
    #ss = login.tembin_login()
    aa, bb = rq_data()
    print(aa)
    print(bb)
