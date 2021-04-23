import pymysql
import readConfig

class DBsql():
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def ConnectDB(self):
        global conn
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except:
            print('数据库连接失败')
        return conn

    def SelectDB(self,query):
        conn = self.ConnectDB()
        #获取游标
        cur = conn.cursor()
        cur.execute(query)
        while 1:
            res=cur.fetchone()
            if res is None:
                #表示已经取完结果集
                break
            print (res)
        conn.commit()
        conn.close()
        print('sql执行成功')


if __name__ == '__main__':
    a = "select * from ad_info;"
    DBsql(readConfig.ReadConfig().get_content('DATABASE','host'),
            readConfig.ReadConfig().get_content('DATABASE','user'),
            readConfig.ReadConfig().get_content('DATABASE','password'),
            readConfig.ReadConfig().get_content('DATABASE','database')).SelectDB(a)