#coding:utf-8
import pymysql

# 打开数据库 （如果连接失败会报错）

# db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'minbo', passwd = '123456', db = 'pythontest')

con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='167710ww', db='test', charset="utf8")

cur = con.cursor()

cur.execute('DROP TABLE person')

cur.execute('CREATE TABLE person (id int not null auto_increment primary key,name varchar(20),age int)')

data = "'wuwei',22"

cur.execute('INSERT INTO person (name,age) VALUES (%s,%s)',('wuwei',22))

cur.executemany('INSERT INTO person (name,age) VALUES (%s,%s)',[('marry',20),('jack',21)])

con.commit()

#con.rollback()

cur.execute('SELECT * FROM person')

res = cur.fetchall()
for line in res:
    print(line)
cur.execute('SELECT * FROM person')
res = cur.fetchone()
print(res)

cur.execute('UPDATE person SET name=%s WHERE id=%s', ('rose',1))
cur.execute('DELETE FROM person WHERE id=%s', (0,))
con.commit()
con.close()


