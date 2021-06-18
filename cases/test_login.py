import unittest
from ddt import ddt, data
from utils.handle_data import data_obj


@ddt
class TestLogin(unittest.TestCase):
    """登录接口测试用例逻辑"""

    cases = data_obj.get(sheet='login')

    @data(*cases['normal'])
    def test_login_success(self, case):
        """
        登录成功
        :return: None
        """
        # first step：获取用例数据
        # second step：请求接口，获取响应
        # third step：断言结果
        print(case)

    @data(*cases['except'])
    def test_login_fail(self, case):
        """
        登录失败
        :return: None
        """
        print(case)
