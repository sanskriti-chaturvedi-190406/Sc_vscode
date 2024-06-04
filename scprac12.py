'''
Programme to read, write and append a csv file.
'''

import csv 

def fread():
    with open('demo_csv.csv', mode="r") as csv_file: 
        reader = csv.reader(csv_file) 
        for item in reader:
            print(item)
            
def fwrite():
    column_name = ["Name", "Sex", "Age", "Height (in)", "Weight (lbs)"] 
    inm=input("Enter name: ")
    isx=input("Enter sex: ")
    iage=int(input("Enter age: "))
    iht=int(input("Enter height: "))
    iwt=int(input("Enter weight: "))
    data = [ inm, isx, iage, iht, iwt] 
    with open('demo_csv.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(column_name) 
        writer.writerow(data) 
        
def fappend():
    field_names = ['Name','Sex','Age','Height (in)','Weight (lbs)']
    inm=input("Enter name: ")
    isx=input("Enter sex: ")
    iage=int(input("Enter age: "))
    iht=int(input("Enter height: "))
    iwt=int(input("Enter weight: "))
    dict = {"Name": inm, "Sex":isx,"Age":iage, "Height (in)":iht, "Weight (lbs)": iwt}
    with open('demo_csv.csv', 'a') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
        dict_object.writerow(dict)

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
