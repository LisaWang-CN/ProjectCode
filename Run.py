import os
import time
import shutil
import pytest

from commons.allureUtil import allureUtil

if __name__ == '__main__':
    # pytest.main(['-vs'])

    pytest.main(["-vs" , '--alluredir=./temp', '--clean-alluredir'])
    time.sleep(3)
    os.system("allure generate ./temp -o ./report --clean")

    allureUtil().doAllureCustom()



    # , '--clean-alluredir'

    # time.sleep(3)
    # os.system("allure generate ./reprt/temps -o ")

    # print(read_case_yaml("./testcases/test_Juhe_post_login.yaml"))
