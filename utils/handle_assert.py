import unittest
from jsonpath import jsonpath


class HandleAssert(unittest.TestCase):
    """封装请求响应断言"""

    def validate(self, expect=None, actual=None):
        """
        断言方法
        :param expect: 期望结果的字典
        :param actual:实际结果的字典
        :return: None
        """
        for t, options in expect.items():
            if t == 'equal':
                for key, value in options.items():
                    self.assertEqual(value, jsonpath(actual, '$..{}'.format(key))[0])
            elif t == 'in':
                for key, value in options.items():
                    self.assertIn(value, jsonpath(actual, '$..{}'.format(key))[0])


assert_obj = HandleAssert()
