import openpyxl
from utils.path import DATA_DIR


class GetCaseData:
    """从各种数据源读取用例数据"""

    def get(self, file=None, sheet=None):
        """
        根据配置的数据源信息，执行相关数据读取方法
        :return: 获取数据方法执行对象
        """
        if file.endswith('.xlsx'):
            data_file = DATA_DIR + '\\excel\\' + file
            return self.get_excel_data(filename=data_file, sheet=sheet)
        elif file.endswith('.py'):
            data_file = DATA_DIR + '\\python\\' + file
            return self.get_python_data(data_file)

    def get_excel_data(self, filename=None, sheet=None):
        """
        读取excel用例数据集并返回
        :param filename: 数据保存excel文件名称
        :return: 用例数据集
        """
        excel_obj = openpyxl.load_workbook(filename)
        sheet_obj = excel_obj[sheet]
        data_set = list(sheet_obj.rows)

        keys = data_set[0]
        keys = [key.value for key in keys]

        data = {'normal': [], 'except': []}
        for values in data_set[1:]:
            item = dict(zip(keys, [value.value for value in values]))
            data['normal'].append(item) if item['type'] == 'normal' else data['except'].append(item)
        return data

    def get_python_data(self, filename=None):
        """
        读取python用例数据集并返回
        :param filename: 数据保存python文件名称
        :return: 用例数据集
        """
        str_datas = ''
        with open(file=filename, mode='r', encoding='utf-8') as f:
            for line in f.readlines():
                str_datas += line
            data_set = eval(str_datas)

        data = {'normal': [], 'except': []}
        for values in data_set[1:]:
            item = dict(zip(data_set[0], values))
            data['normal'].append(item) if item['type'] == 'normal' else data['except'].append(item)
        return data


data_obj = GetCaseData()
