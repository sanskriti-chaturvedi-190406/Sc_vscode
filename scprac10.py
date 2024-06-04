'''
Program to count the no. of vowels present in a file story.txt. If the story.txt contents are as follows:
My first book 
was Me and
My Family. It
gave Me
a chance to be
Known to the 
world.
--------------
The output should read :
Total no. of Vowels =  21
'''

def countv():
    num=0
    f=open("story.txt","r")
    n=f.read()
    for x in n.lower() :
        if x in ['a','e','i','o','u']:
            num=num+1
    f.close()
    print("Total no. of Vowels = ", num)

countv()