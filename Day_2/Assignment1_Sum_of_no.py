# n1 = int(input("Enter the no. = "))
#
# sum = 0
#
# for i in range(0, n1):
#     x = n1 % 10
#     sum = sum + x
#     n1 = n1 // 10
#
# print(sum)


##PRime number

for num in range(2,101):

    prime = True
    for i in range(2,int(num ** 0.5)+1):
        if num % i ==0:
            prime = False
            break

    if prime:
        print(num,end =" ")