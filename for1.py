result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
j=0
for i in result:
    if i=='heads':
        j=j+1
print(j)

print("Printing square of all numbers between 1 to 10 except even numbers")
def square(x):
    x=x**2
    print(x)

for i in range(1,10):
    if i%2 != 0:
        square(i)

print("program 3")
expense_list_value= [2340, 2500, 2100, 3100, 2980]
month_list_key=["Jan","Feb","Mar","Apr","May"]
d={}
for i in month_list_key:
    for j in expense_list_value:
        d[i]=j
        expense_list_value.remove(j)
        break

print(d)
    
print("program 4")
for i in range(5):
    print(f"you ran {i+1} miles")
    tired=input("Are you tired?")
    if tired == 'yes':
        break
if i==4:
    print("you finished 5km race")
else:
    print("you didn't finished 5km race")


print("program 5")
for i in range(1,6):
    s=' '
    for j in range(i):
        s+='*'
    print(s)






































    





































