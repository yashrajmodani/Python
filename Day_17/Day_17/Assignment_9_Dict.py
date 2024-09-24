dict1 = {'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

#Total number of students in the list
print(len(dict1))

#Change Lisa favourite color

dict1['Lisa'] = 'Green'
print(dict1)

#Remove Jenny and her favourite color
del dict1['Jenny']
print(dict1)

#sort and print students and their favourite color alphabetically by name
#
# dict1 = sorted(dict1.items())
# print(dict1)
for key , values in sorted(dict1.items()):
    print(f'{key} : {values}')