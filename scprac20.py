"""
MySQL Connector- Program to select records of students whose percentage > 75, from table student.
"""
import mysql.connector

mydb= mysql.connector.connect(
    host="host", 
    user="username",
    passwd="password",
    database="mydatabase"
)

cursor=mydb.cursor()
cursor.execute("""
    SELECT * FROM student WHERE marks > 75;          
""")

rec=cursor.fetchall()
for x in rec:
  print(x)
  
mydb.commit()