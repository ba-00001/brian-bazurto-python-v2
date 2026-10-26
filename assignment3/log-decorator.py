# Task 1: Writing and Testing a Decorator
import logging

# one time logger setup, everything goes to ./decorator.log
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # use "none" when nothing was passed, otherwise log what came in
        positional = list(args) if args else "none"
        keyword = kwargs if kwargs else "none"
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {positional}")
        logger.log(logging.INFO, f"keyword parameters: {keyword}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper


# no parameters, returns nothing
@logger_decorator
def say_hello():
    print("Hello, World!")


# any number of positional arguments, returns True
@logger_decorator
def takes_positional(*args):
    print(f"Got {len(args)} positional arguments")
    return True


# keyword arguments only, returns the decorator itself
@logger_decorator
def takes_keywords(**kwargs):
    print(f"Got {len(kwargs)} keyword arguments")
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    takes_positional(1, "two", 3.0)
    takes_keywords(name="Brian", course="Python 100", week=3)
    print("Done. Check decorator.log for the results.")
