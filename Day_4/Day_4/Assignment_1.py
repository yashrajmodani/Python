# n=int(input("enter how many pairs you want to add:"))
#
# list = []
# dict ={}
#
# for i in range(n):
#     k=input("enter thew key:")
#     v=input("enter the value:")
#     tup=(k,v)
#     list.append(tup)
#     print(list)
#
# for tup in list:
#     dict.update({tup[0]:tup[1]})
#
# print(dict)


num = int(input("Enter how many pairs you want to add"))

list1 = []
dict1 = {}

for i in range(num):
    k = input("enter thew key:")
    v = input("enter the value:")
    tup = (k,v)
    list1.append(tup)

for tup in list1:
    dict1.update({tup[0]:tup[1]})

print(dict1)
