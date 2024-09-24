num = input("Enter a number: ")

ele = tuple(map(int,num.split(",")))

print(ele)

sort = tuple(sorted(ele))
print(sort)

threshold = int(input("Enter the threshold value : "))

filter_ele = tuple(filter(lambda x: x> threshold, sort))
print(filter_ele)
