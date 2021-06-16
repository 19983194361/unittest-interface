import openpyxl
from utils.path import DATA_DIR
from utils.handle_config import get_config


class GetCaseData:
    """从各种数据源读取用例数据"""

    def __init__(self):
        self.data_info = get_config('data_source')
        self.sheet = None

    def get(self, sheet=None):
        """
        根据配置的数据源信息，执行相关数据读取方法
        :return: 获取数据方法执行对象
        """
        self.sheet = sheet
        data_file = DATA_DIR + '\\' + self.data_info['file_name']
        if self.data_info['file_type'] == 'excel':
            return self.get_excel_data(data_file)

    def get_excel_data(self, filename=None):
        """
        读取excel用例数据集并返回
        :param filename: 数据保存文件名称
        :return: 用例数据集
        """
        # 打开excel文件，查找sheet页，获取所有单元格
        excel_obj = openpyxl.load_workbook(filename)
        sheet_obj = excel_obj[self.sheet]
        data_set = list(sheet_obj.rows)

        keys = data_set[0]
        keys = [key.value for key in keys]

        data = {'normal': [], 'except': []}
        for values in data_set[1:]:
            item = dict(zip(keys, [value.value for value in values]))
            data['normal'].append(item) if item['type'] == 'normal' else data['except'].append(item)
        return data

    # def get_yaml_data(self, file_name=None):
    #     pass
    #
    # def get_py_data(self, file_name=None):
    #     pass
    #
    # def get_sql_data(self):
    #     pass


data_obj = GetCaseData()
