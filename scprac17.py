'''
MySQL Connector- Program to create a connection to the database.
'''

import mysql.connector


mydb= mysql.connector.connect(
    host="host",#Enter host 
    user="username",#Enter your username#
    passwd="password"#Enter your password
)

print(mydb)
    