import pymysql as mq

mysql=mq.connect(host='localhost',user='root',
    password='rashida@123',
    database='amitdb')
mycursor=mysql.cursor()
# print('{:<15}{:<20}{:<10}'.format('Student Id','Student Name','Student Email','Student Class'))

try:
    sql='INSERT INTO student (Id,name) values(%s,%s) ;'
    t=[(3,'zobia'),(4,'heena',)]
    mycursor.executemany(sql,t)
    mysql.commit()
    print("inserteds")
#     sdata=mycursor.fetchall()

#     for i in sdata:
#         print(i)
except:     
    print('error..')