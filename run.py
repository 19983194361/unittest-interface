import unittest
from unittestreport import TestRunner
from utils.common import generate_report

# first step: collect case
suite = unittest.defaultTestLoader.discover(r'cases')

# second step: statement run object, config suite and report param
runner = TestRunner(suite=suite,
                    filename=generate_report(),
                    title='测试报告',
                    tester='蒜苗',
                    desc='测试平台接口自动化执行报告')

# third step: run case
runner.run()
