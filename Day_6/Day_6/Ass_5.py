# import logging
# logging.basicConfig(filename='basicConfig.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s'
# )
#
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is a error message')
# logging.critical('This is a critical message')
#
# #advanced config
#
# logger = logging.getLogger('advancedConfig_logger')
# handler = logging.FileHandler('advancedConfig.log')
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)
#
# logger.debug('debug message')
# logger.info('info message')


import logging


def log_execution():
    logging.basicConfig(filename='basicConfig.log',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s'
                        )

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} Has started")
            result = func(*args, **kwargs)
            logging.debug('This is a debug message')
            logging.info('This is an info message')
            logging.warning('This is a warning message')
            logging.error('This is a error message')
            logging.critical('This is a critical message')

            logger = logging.getLogger('advancedConfig_logger')
            handler = logging.FileHandler('advancedConfig.log')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)

            logger.debug('debug message')
            logger.info('info message')
            print(f"{func.__name__} Has Ended")

        return wrapper

    return decorator


@log_execution()
def hello(name):
    print(f"Hello {name},How are you?")


hello("GreeD")
