def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"This is before The function:{func.__name__}")
        result = func(*args, **kwargs)
        print(f"This is after the function:{func.__name__}")
        return result

    return wrapper


@my_decorator
def helloewcx(name):
    print(f"Hello {name},How are you?")


helloewcx("ufgajc")
