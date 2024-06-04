'''
Programme to remove all the lines that contain the character 'a' in a file and write it to another file.
'''

def read_a():
    global l
    l=[]
    f=open("story.txt","r")
    fl=f.readlines()
    for line in fl:
        for ch in line:
            if ch=='a':
                line=line.replace("\n","")
                l.append(line)
                break
    f.close()
    
def write_a():
    for i in l:
        f=open("story1.txt","a")
        f.write(i)
        f.close()
        f=open("story1.txt","a")
        f.write("\n")
        f.close()

def remove_a():
    global l1
    l1=[]
    f=open("story.txt","r+")
    global fl
    fl=f.readlines()
    a=0
    for line in fl:
        a=line.find("a")
        if a == -1:
            line=line.replace("\n","")
            l1.append(line)
    for i in l1:
        if i==l1[0]:
            f=open("story.txt","w")
            f.write(i)
            f.close()
            f=open("story.txt","a")
            f.write("\n")
            f.close()
        else:
            f=open("story.txt","a")
            f.write(i)
            f.close()
            f=open("story.txt","a")
            f.write("\n")
            f.close()

read_a()
write_a()
remove_a()



