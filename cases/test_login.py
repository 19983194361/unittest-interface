import unittest
from ddt import ddt, data
from utils.handle_data import data_obj
from utils.handle_request import send
from utils.handle_assert import assert_obj
from utils.handle_log import logger


@ddt
class TestLogin(unittest.TestCase):
    """
    登录接口测试用例逻辑
    # first step：获取用例数据
    # second step：请求接口，获取响应
    # third step：断言结果
    """

    # cases = data_obj.get(file='platform.xlsx', sheet='login')
    # cases = data_obj.get(file='login.py')
    cases = data_obj.get(file='login.yaml')

    @data(*cases['normal'])
    def test_login_success(self, case):
        """
        登录成功
        :return: None
        """
        name = case['name']
        try:
            logger.info('[{}]开始执行用例！'.format(name))
            response = send(case=case)
            logger.info('[{}]请求成功！'.format(name))
        except Exception as e:
            logger.error('[{}]请求失败！\r{}'.format(name, e))
            raise e

        assert_obj.validate(expect=eval(case['expect']), actual=response, name=name)

    @data(*cases['except'])
    def test_login_fail(self, case):
        """
        登录失败
        :return: None
        """
        name = case['name']
        try:
            logger.info('[{}]开始执行用例！'.format(name))
            response = send(case=case)
            logger.info('[{}]请求成功！'.format(name))
        except Exception as e:
            logger.error('[{}]请求失败！\r{}'.format(name, e))
            raise e

        assert_obj.validate(expect=eval(case['expect']), actual=response, name=name)
