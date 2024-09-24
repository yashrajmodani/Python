import logging


def log_to_file(log_file="fkhvjgvj.log", log_level = logging.DEBUG):

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    def decorator(func):

        def wrapper(*args, **kwargs):
            logging.debug( f"starting {func.__name__}")
            result= func(*args, **kwargs)
            logging.debug( f"Finished{func.__name__}")
            return result
        return wrapper
    return decorator

@log_to_file()
def hello(name):
    print(f"Hello {name},How are you?")

hello("ufgajc")