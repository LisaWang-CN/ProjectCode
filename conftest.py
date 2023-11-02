# -*- coding: utf-8 -*-
import time

import allure
import pytest

from commons.readyaml import ReadYamlData
from base.removefile import remove_file
from conf.operationConfig import OperationConfig
from conf.setting import dd_msg
from commons.recordlog import logs, apilog, logsNoFormartter

import warnings

conf = OperationConfig()
yfd = ReadYamlData()

#setup 是一个普通的 fixture，在每个用例中可以被调用。它在每个测试方法之前进行初始化操作，并且返回 data 列表。
@pytest.fixture
def setup():
    # 在测试之前的初始化操作
    pass

#global_data 是一个 scope="session" 的 fixture，它在整个测试会话期间只执行一次初始化操作，并且可以在多个测试文件中共享。
@pytest.fixture(scope="session",autouse=True)
def global_data():
    # 禁用HTTPS告警，ResourceWarning
    warnings.simplefilter('ignore', ResourceWarning)

    yfd.clear_yaml_data()
    remove_file("./report/temp", ['json', 'txt', 'attach', 'properties'])

#setup_before_each_test 是一个 autouse=True 的 fixture，它将在每个测试方法之前自动运行。
@pytest.fixture(autouse=True)
def setup_before_each_test():
    # 在每个测试方法之前执行的夹具
    logs.info("------------- 接口测试开始 --------------")
    yield
    logs.info("------------- 接口测试结束 --------------")
    logsNoFormartter.info(" ")

#此外，conftest.py 还可以包含一些 pytest_configure 和 pytest_unconfigure 函数，用于进行 pytest 的全局配置和最终操作。
def pytest_configure():
    # 对 pytest 进行全局配置
    print("Running pytest_configure")

def pytest_unconfigure():
    # 在 pytest 完成后执行一些最终操作
    print("Running pytest_unconfigure")

#注意，conftest.py 中的 fixture 定义和钩子函数可以根据测试需求进行自定义和扩展。 pytest 会自动识别并加载 conftest.py 文件中的配置和夹具。