# para = "Lorem Ipsum passages and more recently with desktop publishing software" \
#        " like Aldus PageMaker including versions of Lorem Ipsum."
# l1 = para.split(" ")
# print(l1)
# for i in range(len(l1)):
#     if i %2 == 1:
#         l1[i] = "replaced"
#
# print(" ".join(l1))
#------------------------------------------
para = "Lorem Ipsum passages and more recently with desktop publishing software" \
       " like Aldus PageMaker including versions of Lorem Ipsum."

l1  = para.split(" ")
for i in range(len(l1)):
    if i %2==1:
        l1[i] = 'replaced'

print(l1)
# print(" ".join(l1))
















