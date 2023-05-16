f=input("enter what factorial you want to find: ")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

if type(f) == float or f < 0:
    print("Argument is not a non-negitive integer")
else:
    num=int(f)+1
    
    

for i in range(1,num):
    print(i, factorial(i))

'''
try:
    print(factorial(-1))
except:a
    print("Argument is not a non-negitive integer")

try:
    print(factorial(1.354))
except:
    print("Argument is not a non-negitive integer")'''

    
    
