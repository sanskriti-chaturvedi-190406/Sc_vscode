'''
MySQL Connector- Program to create a table with user inputs.
'''
import mysql.connector

mydb= mysql.connector.connect(
    host="host", 
    user="username",
    passwd="password",
    database="mydatabase"
)

mycursor=mydb.cursor()
mycursor.execute("""
CREATE TABLE student(
    ROLL NO integer,
    NAME varchar(30),
    CLASS varchar(2),
    SECTION varchar(2),
    MARKS numeric(5,2)
)              
""")

def ins():
    c="y"
    while c in "Yy":
        r=int(input("Enter roll no.: "))
        n=input("Enter name: ")
        c=input("Enter class: ")
        s=input("Enter section: ")
        m=input("Enter marks: ")

        mycursor.execute(f"""
            INSERT INTO student VALUES(
                nsme={n}, class={c}, section={s}, marks={m};
            )
        """)
        c=input("Would you like to continue inserting records?(y/n): ")

ins()
mydb.commit()