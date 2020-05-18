#coding:utf-8
import sqlite3
#open SQL file
con = sqlite3.connect('test.db')
#creat SQL file in memory
#con = sqlite3.connect(':memory:')

#creat SQL link object

#use cursor() to create a cursor object
#use commit() to commit transaction
#use rollback() to rollback transaction
#use close() to close link
cur = con.cursor()

#create table
cur.execute('CREATE TABLE person (id integer primary key,name varchar(20),age integer)')

#insert data
data = "0,'qiye',20"
#cur.execute('INSERT INTO person VALUES (%s)' % data)
#up is very dangerous,we can use placeholder '?'
cur.execute('INSERT INTO person VALUES (?,?,?)' ,(0,'qiye',20))
#we can also use executemany() to execute many SQL codes
cur.executemany('INSERT INTO person VALUES (?,?,?)' ,[(3,'marry',20),(4,'jack',20)])

#then we use commit() to let commit go int effect
con.commit()

#if take mistake,we can rollback
#con.rollback()

#Select data
cur.execute('SELECT * FROM person')
#fetchall() get all data,fetchone() get one
res = cur.fetchall()
for line in res:
    print(line)
cur.execute('SELECT * FROM person')
res = cur.fetchone()
print(res)


#updata and delete data

cur.execute('UPDATE person SET name=? WHERE id=?', ('rose',1))
cur.execute('DELETE FROM person WHERE id=?', (0,))
con.commit()
con.close()

#if you want to update chinese SQL,you need add 'u' before codes
