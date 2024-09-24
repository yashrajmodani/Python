l = []
n = int(input("Enter the positive number = "))

for i in range(2,n):
    for j in range(2,n):
        if n %i==0:
            break
        else:
            print(i)