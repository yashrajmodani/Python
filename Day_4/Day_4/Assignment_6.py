# l1 = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
#
# d1 ={x:l1.count(x) for x in l1}
# print(d1)
#
# # --------------------------------------------------
# sent = input("Enter a sentence: ").split(' ')
# print(sent)
#
# dict1 = {i:len(i) for i in sent}
# print(dict1)


#---------------------------------------

keys = ["name",'age','city']
values = ['Alice',25,'NY']

d1 = dict(zip(keys,values))
print(d1)

dict1 = {keys[i]:values[i] for i in range(len(keys))}
print(dict1)