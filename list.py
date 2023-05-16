E=[2200,2350,2600,2130,2190]
M=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

F_J=E[1]-E[0]

J_F_M=E[0]+E[1]+E[2]


n=input("Please enter the expense of month according to month order seperated by space: ")
X=n.split()
print(X)
for j in range(len(X)):
    E.append(int(X[j]))
    
for i in range(len(E)):
    if E[i] == 2000:
        print("You spent exactly 2000 dollars in the month of:",M[i])


C=int(input("Enter the month you need to correction: "))
C=C-1
amount=int(input("Enter the amount to be sub: "))
E[C]=E[C]-amount

print("All the month expenses in month order are: ",E)    
print("In Feb,how many dollars you spent extra compare to Jan are: ",F_J)
print("Your total expense in first quarter (first three months) of the year are: ",J_F_M)
print(f"Correct expense of month {C} are {E[C]}")


H=['spider man','thor','hulk','iron man','captain america']

print("Length of the heroes list: ",len(H))

h_name=input("Enter the hero name: ")
H.append(h_name)
print("List after adding hero name: ",H)

H.remove('black panther')
print("List after removing hero name: ",H)

H.insert(3,'black panther')
print("List after adding hero name after hulk: ",H)

H[1:3]=['doctor stranger']
print("List after adding hero name doctor stranger: ",H)

H.sort()
print("List after sorting hero names: ",H)





























 
