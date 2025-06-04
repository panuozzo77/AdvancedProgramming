'''
Task: Create a function decorator named @log_time that measures the execution time of the decorated function and prints it to the console.
◦
Requirements:
▪
The decorator should take the function as an argument and return a wrapper function
.
▪
Use the @functools.wraps decorator on the wrapper function to preserve the original function's name and docstring
.
▪
The wrapper should record the time before and after calling the original function
.
▪
It should print a message like "Function function_name executed in duration seconds"
.
▪
The wrapper must handle any number of positional (*args) and keyword (**kwargs) arguments passed to the original function and return the correct result
.
◦
Concepts Applied: Function decorators
, wrapper functions, @ syntax, @functools.wraps, *args and **kwargs.
'''

import time
from asyncio import wait


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'{func.__name__} took {execution_time} seconds')
        return result
    return wrapper

@log_time
def do_something():
    time.sleep(3)

if __name__ == '__main__':
    do_something()