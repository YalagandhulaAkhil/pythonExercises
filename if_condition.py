india=['mumbai','banglore','chennai','delhi']
pakistan=['lahore','karachi','islamabad']
bangladesh=['dhaka','khulna','rangpur']

city_name=input("enter name of city: ")
if city_name in india:
    print("india")
elif city_name in pakistan:
    print("pakistan")
elif city_name in bangladesh:
    print("bangladesh")
else:
    print("city name is not in these 3 countries")


cities_name=input("enter the name of cities: ")
new_list=cities_name.split()
if new_list[0] in india and new_list[1] in india:
    print("both cities are in india")
elif new_list[0] in pakistan and new_list[1] in pakistan:
    print("both cities are in pakistan")
elif new_list[0] in bangladesh and new_list[1] in bangladesh:
    print("both cities are in bangladesh")
else:
    print("both cities are from different countries")
    


