import logging
import time
from functools import wraps

logging.basicConfig(
    filename="my_log_file.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_execution_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        logging.info(f"Function {func.__name__}, executed in {execution_time:.4f} seconds")

        return result

    return wrapper


@log_execution_time
def my_function(name):
    print(f"This is my function{name}")
    
    time.sleep(2)


my_function("GreeeD")
