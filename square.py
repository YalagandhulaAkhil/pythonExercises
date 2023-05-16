'''
num = int(input("enter the number of squares you want: "))
def Square():
    for i in range(1, num+1, +1):
        n=i*i
        print(n, end=" ")

Square()
'''

def next_square():
    i=1
    while True:
        yield i*i
        i += 1

for n in next_square():
    if n>25:
        break
    print(n)
    

