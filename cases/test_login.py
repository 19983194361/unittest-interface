import unittest
import requests
from ddt import ddt, data
from utils.handle_data import data_obj
from utils.handle_config import get_config


@ddt
class TestLogin(unittest.TestCase):
    """登录接口测试用例逻辑"""

    base_url = get_config('environment')
    cases = data_obj.get(sheet='login')

    @data(*cases['normal'])
    def test_login_success(self, case):
        """
        登录成功
        :return: None
        """
        # first step：获取用例数据
        """{'id': 1, 'type': 'normal', 'name': '用户名和密码正确', 'method': 'POST', 'path': 'user/login/',
         'headers': '{"Content-Type": "application/json"}', 'param': None, 'data': None,
         'json': '{"username": "admin", "password": "123456"}', 'expect': '{"code": 0, "username": "admin"}',
         'result': None}"""
        name = case['name']
        method = case['method']
        url = self.base_url['base_url'] + case['path']
        param = case['param']
        data = case['data']
        json = eval(case['json'])
        headers = eval(case['headers'])
        expect = eval(case['expect'])
        # second step：请求接口，获取响应
        response = requests.post(url=url, json=json, headers=headers).json()
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
