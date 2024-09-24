
def factorial(num):
    # print(num)
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


res = factorial(5)
print(res)
