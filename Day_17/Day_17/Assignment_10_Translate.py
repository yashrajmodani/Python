# vowels = ["a","e","i","o","u"]
# def translate(text):
#
#
#
#
import re


text = "This is fun"
pattern = re.sub("[aeiou]",'abc',text)
print(pattern)