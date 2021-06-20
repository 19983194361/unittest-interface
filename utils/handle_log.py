import logging
import time
from utils.handle_config import get_config
from utils.path import LOG_DIR


class HandleLog:
    # 读取日志收集等级配置
    level = get_config('log_level')
    user = get_config('environment')['executor']

    def record_by_file(self):
        """
        收集日志到文件中
        :return: 日志收集对象
        """
        # 声明日志收集对象
        logger = logging.getLogger(self.user)
        logger.setLevel(level=self.level['global'])
        # 声明日志输出渠道和日志等级
        file_path = LOG_DIR + '\\' + '{}.log'.format(time.strftime('%Y%m%d', time.localtime()))
        file_handler = logging.FileHandler(filename=file_path, mode='a', encoding='utf-8')
        file_handler.setLevel(level=self.level['file'])
        # 设置日志格式
        formatter = logging.Formatter(
            fmt='%(asctime)s - executor: %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger


logger = HandleLog().record_by_file()
