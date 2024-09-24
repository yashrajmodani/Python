import re

text = "start my phone number start is (123) 456-7890 and my friend's number end is 098-765-4321 end"



# con=re.findall(r'^start',text)
# print(con)
# result = re.findall(r'end$',text)
# print(result)

matches = re.match(r'^start.*end$',text)
print(matches)