import sectform
x_1= int(input("Enter x1: "))
y_1= int(input("Enter y1: "))
x_2= int(input("Enter x2: "))
y_2= int(input("Enter y2: "))
m_1= int(input("Enter m1: "))
m_2= int(input("Enter m2: "))
a= sectform.sectformx(x_1,x_2,m_1,m_2)
b= sectform.sectformy(y_1,y_2,m_1,m_2)
print("(",a,",",b,")")