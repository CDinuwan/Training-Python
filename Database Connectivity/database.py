import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="Chnauka",password="1234",database="POS")
mycursor=mydb.cursor()

mycursor.execute("show databases")

result=mycursor.fetchall()

result=mycursor.fetchone()

for i in mycursor:
    print(i)

mycursor.execute("select * from student")