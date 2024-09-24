prime_numbers = [x for x in range(2, 50) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

print(prime_numbers)
#
# # x = 37
# # for y in range(2, int(x**0.5) + 1):
# #     if x % y !=0:
# #         print(y)
#
# # x = 83
# # v = int(x**0.5)+1
# # print(v)
#
# n = int(input("Enter a number: "))
# if n < 2:
#     print("Not a prime number")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")