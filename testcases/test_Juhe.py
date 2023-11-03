import allure
import pytest
from commons.readyaml import get_testcase_yaml
from base.apiutil import RequestBase
from base.generateId import m_id, c_id

@allure.feature(next(m_id) + "聚合API测试模块1")
@pytest.mark.run(order=1)
class TestJuhe:

    @allure.story(next(c_id) + '登录接口')#定义用例模块名称
    @pytest.mark.run(order=1)
    # @allure.severity("critical")  # 用例等级（blocker critical normal minor trivial）
    @pytest.mark.parametrize("base_info,testcase", get_testcase_yaml("./testcases/test_Juhe_post_login_new.yaml"))
    def test_post_login(self, base_info,testcase):
        allure.dynamic.title(testcase["case_name"])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "取得用户信息")  # 定义用例模块名称
    @pytest.mark.run(order=2)
    # @allure.severity("normal")  # 用例等级（blocker critical normal minor trivial）
    @pytest.mark.parametrize("base_info,testcase", get_testcase_yaml("./testcases/test_Juhe_UserInfo_new.yaml"))
    def test_get_UserInfo(self,base_info,testcase):
        allure.dynamic.title(testcase["case_name"])
        RequestBase().specification_yaml(base_info, testcase)
