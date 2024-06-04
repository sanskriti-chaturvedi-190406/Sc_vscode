'''
MySQL Connector- Program to create a database and check whether it exists or not.
'''

import mysql.connector

def createdb():
    mydb= mysql.connector.connect(
        host="host",#Enter host 
        user="username",#Enter your username#
        passwd="password"#Enter your password
    )
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")
    
def verification():
    mydb= mysql.connector.connect(
        host="host", 
        user="username",
        passwd="password"
    )
    mycursor=mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)
    
createdb()
verification()

