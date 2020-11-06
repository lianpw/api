import pymysql
import config


class ReadDb:
    # 定义连接对象
    conn = None

    # 获取连接对象方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.Connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PASSWORD, database=config.DB_DATABASE, charset='utf8')
        return self.conn

    # 获取游标对象方法封装
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标对象方法封装
    def close_cursor(self):
        if

