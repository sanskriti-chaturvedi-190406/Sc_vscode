import pickle 
def Write():    
    f = open("Studentdetails.dat", 'wb')     
    while True:         
        r =int(input ("Enter Roll no : "))         
        n = input("Enter Name : ")                  
        record = [r,n,]         
        pickle.dump(record,f)         
        c = input("Would you like to continue writing ?(Y/N)")         
        if c in 'Nn':             
            break         
    f.close() 
        
def Read():     
    f = open("Studentdetails.dat",'rb')     
    try:             
        while True:             
            rec=pickle.load(f)             
            print(rec)     
    except EOFError:         
        f.close() 
        
def ask():     
    f = open("Studentdetails.dat", 'rb+')     
    rollno = int(input("Enter roll no whose record you wish to view"))     
    try:        
        while True:
            pos=f.tell()
            rec = pickle.load(f)
            if rollno== rec[0]:
                f.seek(pos)
                print(f.readline()) 
            c = input("Would you like to continue writing ?(Y/N)")         
            if c in 'Nn':             
                break   
                
    except EOFError: 
        print("INVALID INPUT!")
        print("The roll number entered doesn't exist in the records, please try again.")        
        f.close() 
        
Write() 
Read() 
ask() 