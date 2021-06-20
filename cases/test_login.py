import unittest
from ddt import ddt, data
from utils.handle_data import data_obj
from utils.handle_request import send
from utils.handle_assert import assert_obj


@ddt
class TestLogin(unittest.TestCase):
    """
    登录接口测试用例逻辑
    # first step：获取用例数据
    # second step：请求接口，获取响应
    # third step：断言结果
    """

    cases = data_obj.get(sheet='login')

    @data(*cases['normal'])
    def test_login_success(self, case):
        """
        登录成功
        :return: None
        """
        name = case['name']
        expect = eval(case['expect'])

        response = send(case=case)

        assert_obj.validate(expect, response)

    @data(*cases['except'])
    def test_login_fail(self, case):
        """
        登录失败
        :return: None
        """
        name = case['name']
        expect = eval(case['expect'])

        response = send(case=case)

        assert_obj.validate(expect, response)
