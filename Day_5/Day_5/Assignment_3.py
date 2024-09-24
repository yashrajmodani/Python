# sum = 0
# def num1(*args):
#     var = 0
#     # print(var)
#     for i in args:
#         var += i
#     sum = var
#     print(var)
#     print(sum)
#
#
# # print(sum)
#
# num1(2,34,4,56)
# print(sum)




# ================================
# Assignment 4
counter = 0
def call_function(reset = False):
    global counter

    if reset:
        counter = 0
        print('Counter is reset')
    else:
        counter += 1
        print(f'Function has been called {counter} times')

call_function()
call_function()
call_function(True)
call_function()