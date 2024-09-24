#Docstring
'''This code provide factoral function'''
def factorial(num):
    # print(num)
    """Return 1 if num is 0"""
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


res = factorial(5)
print(res)

print(__doc__)
print(factorial.__doc__)
