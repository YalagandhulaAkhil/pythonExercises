import math
L1=input("enter the subjects seperated by space: ")
L2=input("enter the marks according to subjects squence seperated by space: ")
subjects=list(L1.split())
marks=list(L2.split())
marks=[int(i) for i in marks]
for j in range(len(subjects)):
    print(f"{subjects[j]} ==> {marks[j]}")

def average():
    avg=sum(marks)/len(marks)
    print(avg)

average()
    


