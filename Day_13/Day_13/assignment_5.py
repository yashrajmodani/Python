import re

txt = "The event 12312/02/20046 is scheduled for 16/09/2024 at the conference hall."
pattern = '\s[0-9]{2}\/[0-9]{2}\/[0-9]{4}\s'
res = re.findall(pattern,txt)
print(res)

print('------------------------------------------------------------')
txt1 = 'plsaskmeanything'
res1 = re.sub('ask','tell',txt1)
print(res1)

print('------------------------------------------------------------')

txt2 = 'The cat is on the catalog.The cat is also in the category.'
pattern1 = '\scat\s'
res2 = re.findall(pattern1,txt2)
print(res2)
print( len(res2))


print('------------------------------------------------------------')
txt3 = 'My phone number is 123-456-7890'
# pattern2 = "[0-9]{3}\-[0-9]{3}\-[0-9]{4}"
pattern2 = "[0-9]"
res3 = re.findall(pattern2,txt3)
print(res3)

print('------------------------------------------------------------')
str = " My number is 123,and my friend's number is 4567890."
