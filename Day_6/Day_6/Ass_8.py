# import re
#
# with open('A_8.txt','r')as file:
#     lines = file.readline()
#     print(lines)
#
# text1 = lines.split(" ")
# print(text1)
#
# for i in lines:
#     for j in i:
#         if re.findall(r"^[AEIOUaeiou]\w[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\b"):
#
# #
import re
text= '''
Apple pie is delicious. 
Under the bed, there is a cat! 
Note from the meeting! 
1234a5678b9aaa 
Do not forget to check the details!
'''

pattern = r'^[aeiouAEIOU]\w*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\b'
# pattern = (r'\d+[^\d]')
pattern = (r'^Note.*!$')

matches = re.findall(pattern,text)
print(matches)