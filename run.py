import unittest
from unittestreport import TestRunner
from utils.common import generate_report

# 收集用例
suite = unittest.defaultTestLoader.discover(r'cases')

# 启动程序
runner = TestRunner(suite=suite,
                    filename=generate_report(),
                    title='测试报告',
                    tester='蒜苗',
                    desc='测试平台接口自动化执行报告')

# 执行用例
runner.run()
