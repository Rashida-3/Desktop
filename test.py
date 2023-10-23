import mysql.connector



mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='rashida@123'
    # database='amitdb'
)


mycursor=mydb.cursor()


mycursor.execute('SHOW DATABASES')
for db in mycursor:
    print(db)