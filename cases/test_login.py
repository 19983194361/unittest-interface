import unittest
from utils.handle_data import data_obj


class TestLogin(unittest.TestCase):
    """登录接口测试用例逻辑"""

    cases = data_obj.get(sheet='login')

    def test_login_success(self):
        """
        登录成功
        :return: None
        """
        # first step：获取用例数据
        # second step：请求接口，获取响应
        # third step：断言结果
        print(self.cases['normal'])

    def test_login_fail(self):
        """
        登录失败
        :return: None
        """
        print(self.cases['except'])
