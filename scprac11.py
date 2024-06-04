'''
Programme to read, write and append a text file.
'''

def fread():
    print("1.Only read")
    print("2.Read and write")
    c2=int(input("Enter your choice: "))
    if c2==1:
         f=open('story.txt','r')
         r=f.read()
         print(r)
         f.close()
    elif c2==2:
         f=open('story.txt','r+')
         r=f.read()
         print(r)
         f.seek(0)
         i=input("Enter what you would like to write:")
         f.write(i)
         f.close()
    else:
        print("Invalid input")
        
def fwrite():
    print("1.Only write")
    print("2.Write and read")
    c2=int(input("Enter your choice: "))
    if c2==1:
         f=open('story.txt','w')
         i=input("Enter what you would like to write: ")
         w=f.write(i)
         f.close()
    elif c2==2:
         f=open('story.txt','w+')
         i=input("Enter what you would like to write: ")
         f.write(i)
         f.seek(0)
         r=f.read()
         print(r)
         f.close()
    else:
        print("Invalid input")
        
def fappend():
    print("1.Only append")
    print("2.Append and read")
    c2=int(input("Enter your choice: "))
    if c2==1:
         f=open('story.txt','a')
         i=input("Enter what you would like to append: ")
         f.write(i)
         f.close()
    elif c2==2:
         f=open('story.txt','a+')
         i=input("Enter what you would like to append: ")
         a=f.write(i)
         f.seek(0)
         r=f.read()
         print(r)
         f.close()
    else:
        print("Invalid input")
       
def menu():
    c="y" 
    while c=="y":
        print("1.Read")
        print("2.Write")
        print("3.Append")
        c1=int(input("Enter your choice: "))
        if c1==1:
            fread()
        elif c1==2:
            fwrite()
        elif c1==3:
            fappend()
        else:
            print("Invalid input")
        c=input("Would you like to continue? ")

menu()