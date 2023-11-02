import pytest
import requests

# from commons.request_util import RequestUtil

import allure
import pytest
from commons.readyaml import get_testcase_yaml
from base.apiutil import RequestBase
from base.generateId import m_id, c_id

@allure.feature(next(m_id) + "聚合API测试模块2")
@pytest.mark.run(order=2)
class TestApi:
    @allure.story(next(c_id) + '登录接口')  # 定义用例模块名称
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("base_info,testcase", get_testcase_yaml("./testcases/test_Juhe_post_login_new.yaml"))
    def test_post_login(self, base_info, testcase):
        allure.dynamic.title(testcase["case_name"])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "取得用户信息")  # 定义用例模块名称
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("base_info,testcase", get_testcase_yaml("./testcases/test_Juhe_UserInfo_new.yaml"))
    def test_get_UserInfo(self, base_info, testcase):
        allure.dynamic.title(testcase["case_name"])
        RequestBase().specification_yaml(base_info, testcase)

    # Access_token = ""
    #
    # #登陆
    # @pytest.mark.smoke
    # def test_post_login(self):
    #     urls = "https://api.apiopen.top/api/login"
    #     datas ={"account":"1263482196@qq.com","password":"123456"}
    #     headerss = {
    #         "Sec-Fetch-Mode": "cors",
    #         "Referer": "https://api.apiopen.top/login",
    #         "Sec-Fetch-Site": "same-origin",
    #         "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    #         "Origin": "https://api.apiopen.top",
    #         "Accept": "application/json, text/plain, */*",
    #         "sec-ch-ua": '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    #         "sec-ch-ua-mobile": "?0",
    #         "sec-ch-ua-platform": '"Windows"',
    #         "Content-Type": "application/json",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61",
    #         "Sec-Fetch-Dest":"empty"
    #     }
    #     #res = requests.post(url=urls,json=datas,headers=headerss)
    #     res = RequestUtil().all_send_request("post",url=urls,json=datas,headers=headerss)
    #     TestApi.Access_token = res.json()["result"]["token"]
    #     print(TestApi.Access_token)

    # #取得个人信息
    # def test_get_UserInfo(self):
    #     urls = "https://api.apiopen.top/api/getUserInfo"
    #     headerss = {
    #         "token": TestApi.Access_token
    #     }
    #     res = RequestUtil().all_send_request("get",url=urls,headers=headerss)
    #     #print(res.json())

    #文件上传的例子, 只写了files传参的代码实例，因为没有找到免费接口
    # def test_post_fileUpload(self):
    #     urls = "https://api.apiopen.top/api/media/uploadimg"
    #     headerss = {
    #         "token": TestApi.Access_token
    #     }
    #     datas = {
    #         "media":open("d:\\file.img","rb")
    #     }
    #     res = requests.post(url=urls, headers=headerss, files=datas)
    #     print(res.json())

