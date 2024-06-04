'''
Programme using pickle module- pickle.load and pickle.dump .
'''

import pickle

fd=open('studentdetails.dat','ab')
name=input("Enter the student's name: ")
roll=input("Enter the student's roll no.: ")
marks=input("Enter the student's marks: ")
l=[name, roll, marks]
pickle.dump(l,fd)
fd.close()

fl=open('studentdetails.dat','rb')
pickle.load(fl)
fl.close()