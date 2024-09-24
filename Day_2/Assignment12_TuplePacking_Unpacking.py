# lst=[]
# name = input("Enter the name : ")
# age = int(input("Enter the age : "))
#
# s_tuple = tuple(input("Enter the city name : "))
# s_tuple1 = tuple(input("Enter the country name : "))
#
# tup = tuple(name,age,)
# print(lst)


name = input("Enter your name: ")
age = int(input("Enter your age: "))


city = input("Enter your city: ")
country = input("Enter your country: ")
tup = (city, country)

my_tuple = (name,age,tup)

print(my_tuple)

unpacked_name, unpacked_age, (unpacked_city , unpacked_country) = my_tuple
print(unpacked_name)
print(unpacked_age)
print(unpacked_city)
print(unpacked_country)
