def get_integer_input(x, y):
    try:
        result= x/y
    except ZeroDivisionError:
        print("Error: number cannot be divided by 0")
    except TypeError:
        print("Error: number must be integer")
    else:
        print(f"result is {result}")
    finally:
        print("Operation Complete!")

get_integer_input(10,5)
get_integer_input(10,10)
get_integer_input(10,0)