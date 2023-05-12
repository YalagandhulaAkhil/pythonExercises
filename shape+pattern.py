x=input('please enter what area do you want to find: triangle,rectangle')

if(x == 'triangle'):
    base=int(input('please enter the base:'))
    height=int(input('please enter the height:'))
    area1=(base*height)/2
    print(area1)
    print('here is triangle pattern:')
    for i in range(base):
        s=''
        for j in range(i+1):
            s=s+'*'
        print(s)
elif(x == 'rectangle'):
    length=float(input('please enter the length:'))
    width=float(input('please enter the width:'))
    area2=(length*width)
    print(area2)





