import unittest
from utils.common import get_case_data


class TestLogin(unittest.TestCase):

    cases_data = get_case_data('login.yaml')

    def test_login_success(self):
        """
        登录成功
        :return: None
        """
        # 第一步：获取用例数据
        # 第二步：请求接口，获取响应
        # 第三步：断言结果
        print(self.cases_data['normal'])

    def test_login_fail(self):
        """
        登录失败
        :return: None
        """
        print(self.cases_data['except'])
