import yaml
from utils.path import CONFIG_DIR


def get_config(section=None):
    """
    从配置文件中读取详细配置信息
    :param section: 配置项名称
    :return: 配置项内容
    """
    conf_file = CONFIG_DIR + '\\' + 'conf.yaml'
    with open(file=conf_file, mode='r', encoding='utf-8') as f:
        conf_content = yaml.load(stream=f, Loader=yaml.FullLoader)
        return conf_content[section]
