import pymysql
from utils.handle_config import get_config


class HandleDatabase:
    """数据库连接，数据查询类"""

    db = get_config('mysql')

    def __init__(self):
        """读取数据库相关配置"""
        self.host = self.db['host'],
        self.port = self.db['port'],
        self.database = self.db['database'],
        self.user = self.db['user'],
        self.password = self.db['password']
        self.open()

    def open(self):
        """连接数据库，创建游标对象"""
        self.connect = pymysql.connect(host=self.host,
                                       port=self.port,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
        self.cursor = self.connect.cursor()

    def count(self, sql=None):
        """
        获取查询结果的总数
        :param sql: 查询语句
        :return: 结果总数
        """
        self.connect.commit()
        count = self.cursor.execute(query=sql)
        self.close()
        return count

    def get_one(self, sql=None):
        """
        获取单个查询结果
        :param sql: 查询语句
        :return: 单结果详细信息
        """
        self.connect.commit()
        self.cursor.execute(query=sql)
        result = self.cursor.fetchone()
        self.close()
        return result

    def get_many(self, sql=None):
        """
        获取多个查询结果
        :param sql: 查询语句
        :return: 多结果详细信息
        """
        self.connect.commit()
        self.cursor.execute(query=sql)
        result = self.cursor.fetchmany()
        self.close()
        return result

    def get_all(self, sql=None):
        """
        获取全部查询结果
        :param sql: 查询语句
        :return: 全部结果详细信息
        """
        self.connect.commit()
        self.cursor.execute(query=sql)
        result = self.cursor.fetchall()
        self.close()
        return result

    def close(self):
        """关闭游标对象和数据库连接对象"""
        self.cursor.close()
        self.connect.close()
