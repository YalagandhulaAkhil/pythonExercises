
integer=[0,1,2,3,4]
binary=["0","1","10","11","100"]
binary_dic={}
for key in integer:
    for value in binary:
        binary_dic[key]=value
        binary.remove(value)
        break
print(str(binary_dic))




'''integer=[0,1,2,3,4]
binary=["0","1","10","11","100"]
z=zip(integer,binary)
binary_dic={integer:binary for integer,binary in z}
print(binary_dic)'''

g=[1,-1,2,3,5,0,-7]
add_inverse=[-1*i for i in g]
print(add_inverse)

a=[1,-1,2,-2,3,-3]
sq_set={i*i for i in a}
print(sq_set)




