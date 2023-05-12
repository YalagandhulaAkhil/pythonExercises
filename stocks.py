prices={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
le=len(prices)
my_list=list(prices.values())
a=[]
def print_all():
    for i in range(0,,+1):
        j=(my_list[i][0]+my_list[i][1]+my_list[i][2])/3
        a.append(j)
    i=0
    for s,p in prices.items():
        print(f"{s} ==> {p} ==> {a[i]}")
        i=i+1

def add():
    s=input("please enter the stock ticker to add: ")
    p=input("please enter the price: ")
    p=float(p)
    if s in prices:
        prices[s].append(p)
    else:
        prices[s]=[p]
    print_all()

def main():
    op=input("enter operation(print,add):")
    if op.lower() =='print':
        print_all()
    if op.lower() =='add':
        add()

if __name__ == '__main__':
    main()



































    
            

    
    















































































