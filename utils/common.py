import time
from utils.path import REPORT_DIR


class Temporary:
    """
    临时类，用于存储用例执行过程中的属性值
    """
    pass


def get_current_time():
    """
    返回当前系统时间
    :return: 格式化后的时间
    """
    return time.strftime('%Y%m%d-%H时%M分%S秒', time.localtime())


def generate_report(report_name=None):
    """
    获取测试报告完整的路径与名称
    若report_name参数不为空，则返回用户自定义的报告名称
    若report_name参数为空，则返回默认的报告名称
    :param report_name: 用户传参
    :return: 报告路径与名称
    """
    if report_name:
        return REPORT_DIR + '\\' + report_name
    return REPORT_DIR + '\\' + '测试报告-' + get_current_time()
