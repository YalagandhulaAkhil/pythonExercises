p, c =0, 1
L=int(input("enter the number of iterators: "))
print("fibonacci series: ", p, c, end=" ")
for i in range(2, L):
    r = p + c
    p = c
    c = r
    print(r, end=" ")


                
      
    
