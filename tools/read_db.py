import pymysql
import config


class ReadDb:
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
    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭连接对象方法封装
    def close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    # 主要 执行方法 --> 在外界调用此方法就可以完成数据相应的操作
    def get_sql_one(self, sql):
        # 定义游标对象及数据变量
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)

            # 获取结果
            data = cursor.fetchone()
        except Exception as e:
            print('get_sql_error:', e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    # 获取 所有数据库结果集
    def get_sql_all(self, sql):
        # 定义游标对象及数据变量
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)

            # 获取结果
            data = cursor.fetchall()
        except Exception as e:
            print('get_sql_error:', e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接对象
            self.close_conn()
            # 返回执行结果
            return data

    # 修改, 删除, 新增
    def update_sql(self, sql):
        # 定义游标对象及数据变量
        cursor = None
        data = None
        try:
            # 获取游标对象
            cursor = self.get_cursor()
            # 调用执行方法
            cursor.execute(sql)

            # 提交事务
            self.conn.commit()

        except Exception as e:
            # 事务回滚
            self.conn.rollback()
            print('get_sql_error:', e)
        finally:
            # 关闭游标对象
            self.close_cursor(cursor)
            # 关闭连接对象
            self.close_conn()


if __name__ == '__main__':
    # result = ReadDb().get_sql_one("select * from wm_user")

    # result = ReadDb().get_sql_all("select * from wm_user")

    result = ReadDb().update_sql("update wm_user set username = '静心' where id = '10001673'")

    print(result)
    print(type(result))
