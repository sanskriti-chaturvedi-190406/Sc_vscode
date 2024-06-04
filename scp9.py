'''
Program to create a binary file with roll no., name and marks. also input a roll number and update the marks.
'''

import pickle

def write():
    c="y"
    while c=="y":
        f=open("studentdetails.dat","ab+")
        roll=input("Enter roll no.: ")
        name=input("Enter name: ")
        marks=input("Enter marks: ")
        record=[roll,name,marks]
        pickle.dump(record,f)
        record={}
        f.close()
        read()
        c=input("Would you like to continue writing? (y/n): ")
        
def read():
    f=open("studentdetails.dat","rb+")
    try:
        while True:
            rec=pickle.load(f)
            print(rec)
    except EOFError:
        pass
    f.close()
    
def update():
    c="y"
    while c=="y":
        f=open("studentdetails.dat","rb+")
        roll=input("Enter the roll no. for which you'd like to update marks: ")
        fp=f.tell()
        l=pickle.load(f)
        for i in l:
            if i[0]==roll:
                upmarks=input("Enter updated marks: ")
                i[2]=upmarks
            f.seek(fp)
            pickle.dump(i,f)
        print("Updated record is: ",i)
        f.close()
        c=input("Would you like to continue updating? (y/n): " )
        
def main():
    c="y"
    while c=="y":
        print (" 1. Write",'\n',"2. Update",'\n',"3. Read" )
        c=int(input("Enter choice: "))
        if c==1:
            write()
            #read()
        elif c==2:
            update()
        elif c==3:
            read()   
        else :
            print ("Invalid input")
        c=input("Would you like to continue? (y/n) : ")
        
main()
                