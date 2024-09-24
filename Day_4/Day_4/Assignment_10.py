# strings

str1 = input("enter a string:")
str2 = input("enter a string:")

str1 = str1.lower().strip()
print(str1)
str2 = str2.lower().strip()
print(str2)

str1 = "".join(sorted(str1))
str2 = "".join(sorted(str2))

str1 = " ".join(sorted(str1))
str2 = " ".join(sorted(str2))

print(str1)
print(str2)

if str1 == str2:
    print("ANAGRAMS")
else:
    print("not anagrams")








