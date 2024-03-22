import pymysql

# 创建连接对象
conn = pymysql.connect(host='localhost', port=3306, user='root',
                       password='123456',database='paper', charset='utf8')
# 获取游标对象
cursor = conn.cursor()
sql = "select * from card_data;"

cursor.execute(sql)

for line in cursor.fetchall():
    print(line)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()