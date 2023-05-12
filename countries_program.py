dic={'china':143,'india':136,'usa':32,'pakistan':21}
def printall():
    for c,p in dic.items():
        print(f"{c}==>{p}")

def add():
    c=input('name of the the country: ')
    c=c.lower()
    if c in dic:
        print("country already exist")
        return
    p=float(input("no of population: "))
    dic[c]=p
    printall()

def remove():
    c=input('name of the the country: ')
    c=c.lower()
    if c not in dic:
        print("country does not exist")
        return
    del dic[c]
    printall()

def query():
    c=input('name of the the country: ')
    c=c.lower()
    if c not in dic:
        print("country does not exist")
        return
    print(dic[c])

def main():
    op=input("enter operation that you want: ")
    if op.lower() == 'add':
        add()
    if op.lower() == 'remove':
        remove()
    if op.lower() == 'printall':
        printall()
    if op.lower() == 'query':
        query()


if __name__ == '__main__':
    main()






























    









    
    

    
