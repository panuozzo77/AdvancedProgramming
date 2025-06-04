'''
Task: Create a function decorator factory named @retry(attempts, exceptions) that retries the decorated function call
up to a specified number of attempts if it raises one of the specified exceptions.

Requirements:
retry should be a function that takes attempts (an integer) and exceptions (a tuple of exception types) as arguments
retry should return a function decorator that takes the function to be decorated
The returned decorator should return a wrapper function that implements the retry logic
The wrapper function should call the original function. If it raises an exception included in the exceptions tuple, it should decrement the attempt count and retry after a small delay (e.g., using time.sleep, note: time is outside the provided sources). If attempts run out and the exception persists, re-raise the last exception.

Use @functools.wraps on the wrapper function
The wrapper must handle *args and **kwargs
Concepts Applied: Function decorators
, decorator factories, parameterized decorators, wrapper functions, @functools.wraps, exception handling.
'''
import random


def retry(attempts, exceptions):

    def decorator(func):
        def wrapper(*args, **kwargs):
            remaining_attempts = attempts
            last_exception = None
            while remaining_attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if isinstance(e, exceptions):
                        remaining_attempts = remaining_attempts -1
                        last_exception = e
                        print(f"[Retry] Exception caught: {e}. Attempts left: {remaining_attempts}")
                    else:
                        print("[Retry] All attempts failed.")

            return None

        return wrapper
    return decorator

@retry(attempts=6, exceptions=(ValueError,))
def do_something():
    x = random.randint(1, 10)
    print(f"Generated: {x}")
    if x < 8:
        raise ValueError("Random value too low!")
    return f"Success with {x}"

if __name__ == '__main__':
    do_something()