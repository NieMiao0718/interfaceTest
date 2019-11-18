import readConfig as readConfig

readconfig = readConfig.ReadConfig()

class geturlParams():# 定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self,httptype):
        #new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':' + readconfig.get_http('port') + '/login' + '?'
        if httptype == 'HTTP':
            new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':' + readconfig.get_http('port')
        if httptype == 'HTTP_test':
            new_url = readconfig.get_http_test('scheme') + '://' + readconfig.get_http_test('baseurl') + ':' + readconfig.get_http_test('port')
        return new_url

if __name__ == '__main__':# 验证拼接后的正确性
    print(geturlParams().get_Url('HTTP'))
    print(geturlParams().get_Url('HTTP_test'))

