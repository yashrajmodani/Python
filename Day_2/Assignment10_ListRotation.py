l = []

n = int(input("How many elements you want to add in list = "))

for i in range(1, n + 1):
    list_ele = int(input("Enter the no. to add in list = "))
    l.append(list_ele)

l1 = l.copy()

pos = int(input("Enter the position you want to rotate = "))

print(l1[-pos:]+l1[:-pos])

print(l1)
