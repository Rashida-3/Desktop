import mysql.connector
conn=mysql.connector.connect(host='localhost',password='rashida@123',user='root')
if conn.is_connected():
   print("connection established...")                          

                             
