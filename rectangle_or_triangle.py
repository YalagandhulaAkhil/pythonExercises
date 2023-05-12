x=input('please enter what area do you want to find: triangle,rectangle')

if(x == 'triangle'):
    base=float(input('please enter the base:'))
    height=float(input('please enter the height:'))
    area1=(base*height)/2
    print(area1)
elif(x == 'rectangle'):
    length=float(input('please enter the length:'))
    width=float(input('please enter the width:'))
    area2=(length*width)
    print(area2)

