# Str = input("Enter the no's = ")
# l = []
# Str1 = Str.split(",")
# for i in Str1:
#     l.append(i)
#
# my_tuple = tuple(l)
# print("After converting into tuple = ", my_tuple)
# print("First element of my_tuple is = ", my_tuple[0])
# print("Last element of my_tuple is = ", my_tuple[-1])
#
# print("After slicing second to second last element = ", my_tuple[1:-1])
# print("Every second element of the tuple is = ", my_tuple[1::2])
# print("Reversed Tuple is = ", my_tuple[::-1])
#
#
#


ele = input("Enter the no's: ")
l = []
str1 = ele.split(",")
for i in str1:
    l.append(i)

my_tuple = tuple(l)

print("After converting into tuple: ", my_tuple)
print("First element of the tuple is: ",my_tuple[0])
print("last element of the tuple is: ",my_tuple[-1])
print("After slicing second to second last element of the tuple is: ",my_tuple[1:-1])
print("Every second element of the tuple is: ",my_tuple[1::2])
print('Reversed tuple is: ',my_tuple[::-1])