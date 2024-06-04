import pickle 
def Write():    
    f = open("Studentdetails.dat", 'wb')     
    while True:         
        r =int(input ("Enter Roll no : "))         
        n = input("Enter Name : ")         
        m = int(input ("Enter Marks : "))         
        record = [r,n,m]         
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
        
def Update():     
    f = open("Studentdetails.dat", 'rb+')     
    rollno = int(input("Enter roll no whoes marks you want to update"))     
    try:         
        while True:             
            pos=f.tell()             
            rec = pickle.load(f)             
            if rec[0]==rollno:                 
                um = int(input("Enter Update Marks:"))                 
                rec[2]=um                 
                f.seek(pos)                 
                pickle.dump(rec,f)                 
                #print(rec)     
                
    except EOFError:         
        f.close() 
        
Write() 
Read() 
Update() 
Read()