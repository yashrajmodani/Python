import random
countries = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasilia",
    "China": "Beijing",
    "India": "New Delhi",
    "Italy": "Rome",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "South Africa": "Pretoria"
}
score =0

# x = countries.keys()
# print(x)


for i in countries:
    random_keys = random.choice(list(countries.keys()))
    print(random_keys)
    capital = input("Enter the capital name:")
#
#     if capital == countries[random_keys]:
#         score+=1
#         print("correct answer")
#
#
#     else:
#         print("wrong answer")
#         print("correct answer is : ", countries[random_keys])
#
#
#     choice = input("Do you wish to continue: Y Or N")
#     if choice == "n":
#         print(f"your total score is {score}")
#         break

