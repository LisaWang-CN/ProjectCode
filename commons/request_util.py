import requests

fiddler_proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}

#统一请求封装
class RequestUtil:
        sess =  requests.session()

        #启用代理
        # def all_send_request(self,method,url,**kwargs):
        #     res = RequestUtil.sess.request(method,url,proxies=fiddler_proxies,verify=False,**kwargs)
        #     return res
        #不启用代理
        def all_send_request(self,method,url,**kwargs):
            res = RequestUtil.sess.request(method,url,**kwargs)
            return res