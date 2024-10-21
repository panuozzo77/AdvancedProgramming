def tointeger(function):
    def wrapper(*args, **kwargs):
        try:
            # Convert all arguments to integers
            appoggio = [int(arg) for arg in args]
            return function(*appoggio, **kwargs)  # Return the result of the function
        except (TypeError, ValueError):  # Handle both TypeError and ValueError
            print("Invalid input. Please enter a castable (to integer) value.")
            return None  # Return None if there is an error
    return wrapper

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1  # Simplified base case

@tointeger
def gen_fact(n):
    for i in range(1, n + 1):  # Change range to include n
        yield factorial(i)  # Yield factorial of each i

if __name__ == '__main__':
    n = input("Inserisci un numero: ")
    for x in gen_fact(n):
        if x is not None:  # Check if x is valid before printing
            print(x)
