sugar_value=int(input("enter your sugar value: "))

if sugar_value >=80 and sugar_value <=100:
    print("your sugar is normal")
elif sugar_value < 80:
    print("your sugar is low")
elif sugar_value > 100:
    print("your sugar is high")
