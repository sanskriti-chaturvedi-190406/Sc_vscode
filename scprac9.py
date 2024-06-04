'''
Program to implement a stack.
'''
def stacks():
    l=[]
    c="y"
    while c=="y":
        print("1.Push")
        print("2.Pop")
        print("3.Display")
        f=int(input("Enter your function choice: "))
        if f==1:
            s=input("Enter element to be pushed:")
            l.append(s)
        elif f==2:
            if l==[]:
                print("Stack is empty")
            else:
                print("Removed item is: ",l.pop())
        elif f==3:
            for x in l:
                print(x)
        else:
            print("Invalid input")
        c=input("Would you like to continue? ")
    
stacks()