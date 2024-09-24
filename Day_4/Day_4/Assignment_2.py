list = ["name","name","ok","johnqt","ok","johnqt",True,1,1,2,0,5,23,5,1,False,0]
dict = {}

for i in list:
    counter = list.count(i)
    dict.update({i:counter})

print(dict)

# l1 = input("enter").split(' ')
# dict = {i : l1.count(i) for i in l1}
# print(dict)

