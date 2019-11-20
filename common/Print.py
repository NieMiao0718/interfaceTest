import json
def log_print(method, url, response, data=None, ):
    if method=="get":
        print("**********请求信息**********")
        print("request method:", method)
        print("request url:", url)
    if method=="post":
        print("**********请求信息**********")
        print("request method:", method)
        print("request url:", url)
        data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
        print("request data:", data)
    print("**********结果返回**********")
    print(response)

if __name__ == '__main__':
    log_print("get", "https://www.test.com", "test")
    log_print("post", "https://www.test2.com", "test2", "test_data")
