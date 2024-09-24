
# list1 = []
# n = int(input("Enter no. of items to add:"))
# for i in range(n):
#     item = input("Enter the item: ")
#     quantity = int(input("Enter the quantity: "))
#     price = float(input("Enter the price: "))
#     entry = (item,(quantity,price))
#     list1.append(entry)

# my_dict = dict(list1)
# print(my_dict)

#Assignment 15
# while True:
#     num = int(input("Enter the number of students : "))
#
# #Assignment 16
# while True:
#     num_items = int(input("Enter the number of items : "))
#     dict = {}
#     total = 0
#     sum = 0
#     for i in range(1, num_items +1):
#         item = input("Enter the item : ")
#         quantity = int(input("Enter the quantity : "))
#         price = int(input("Enter the price : "))
#         dict[item] = {'quantity':quantity,'price':price}
#     print(dict)
#     for i,j in dict.items():
#         prod = j['quantity']*j['price']
#         total = total + j['quantity']
#         sum = sum +prod
#     print(f"Total inventory is {total}")
#     print(f"Total inventory cost is {sum}")
#
#
#     cont = input("Do you wish to continue? (y/n) : ")
#     if cont == 'n':
#         print("Exited!")
#         break
#     else:
#         continue


#Assignment 17

# import random
# country_capitals = {
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Germany": "Berlin",
#     "Canada": "Ottawa",
#     "India": "New Delhi",
#     "Brazil": "Brasilia",
#     "Australia": "Canberra",
#     "China": "Beijing",
#     "Italy": "Rome",
#     "Mexico": "Mexico City"
# }
#
# countries = list(country_capitals.keys())
# random.shuffle(countries)
# correct  = 0
# incorrect = 0
# wrong_ans = []
#
# for country in countries:
#     user = input(f'What is the capital of {country}').strip()
#
#     if user.lower() == country_capitals[country].lower():
#         print("Correct")
#         correct += 1
#     else:
#         print("Incorrect")
#         incorrect += 1
#         wrong_ans.append((country,user,country_capitals[country]))
#
# total_questions = correct + incorrect
# score_percentage = (correct / total_questions) * 100
# if incorrect > 0:
#     print("\nIncorrect answers summary:")
#     for country, user_answer, correct_answer in wrong_ans:
#         print(f"Country: {country}, Your answer: {user}, Correct answer: {correct}")
#

# Assignment 18: Build a simple phonebook application using dictionaries.

# while True:
#     num_items = int(input("Enter the number of items : "))
#     dict = {}
#     for i in range(1, num_items +1):
#         name = input("Enter the name : ")
#         phone = int(input("Enter the phone number : "))
#         email = input("Enter the email : ")

#         value = (phone,email)
#         dict[name] = value
#     print(dict)

#     choice = input("Enter the choice \n\t1) Add \n\t2)search \n\t3)update \n\t4)delete")
#     match choice:
#         case "1":
#             name = input("Enter the name : ")
#             if name in dict:
#                 print("Name already exists")
#             else:
#                 phone = int(input("Enter the phone number : "))
#                 email = input("Enter the email : ")
#                 value = (phone,email)
#                 dict.update({name:value})
#                 print(dict)
#         case "2":
#             name = input("Enter the name : ")
#             if name in dict:
#                 print(dict[name])
#             else:
#                 print("Name not found")
#         case "3":
#             name = input("Enter the name : ")
#             if name in dict:
#                 phone = int(input("Enter the phone number : "))
#                 email = input("Enter the email : ")
#                 value = (phone, email)
#                 dict.update({name: value})
#         case "4":
#             name = input("Enter the name : ")
#             if name in dict:
#                 del dict[name]
#                 print(dict)
#             else:
#                 print("Name not found")



#Assignment_19

# list = ['name','hi','name','hello','hi','salim',6,7,8,5,3,6,7,5,True]
# dict = {}
# # l1 = input('enter').split(',')
# #
# for i in list:
#     counter = list.count(i)
#     dict.update({i:counter})
#
# print(dict)
#
#


#Assignment14

sent = input("Enter a sentence: ").split(' ')
print(sent)

dict1 = {i:len(i) for i in sent}
print(dict1)