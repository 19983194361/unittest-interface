import unittest
from ddt import ddt, data
from utils.handle_data import data_obj
from utils.handle_request import send


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
        name = case['name']
        expect = eval(case['expect'])
        # second step：请求接口，获取响应
        response = send(case=case)
        # third step：断言结果
        self.assertEqual(response['code'], expect['code'])
        self.assertEqual(response['data']['username'], expect['username'])

    @data(*cases['except'])
    def test_login_fail(self, case):
        """
        登录失败
        :return: None
        """
        print(case)
