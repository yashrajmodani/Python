Str = input("Enter the no's = ")

str1 = tuple(map(int,Str.split(",")))
print(str1)

total_sum = sum(str1)
print(total_sum)
avg = total_sum/len(str1)
print(avg)
max_value = max(str1)
print(max_value)
min_value = min(str1)
print(min_value)
num_elements = len(str1)
print(num_elements)



