import datetime

def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for i in range(times-1):
                function(*args, **kwargs)
            return function(*args, **kwargs)
        return wrapper
    return decorator


def checker(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            counter = 0

            # Controllo degli argomenti posizionali
            for arg in args:
                if isinstance(arg, type):
                    counter += 1

            # Controllo degli argomenti keyword
            for key, value in kwargs.items():
                if isinstance(value, type):
                    counter += 1

            print(f'Contati: {counter} argomenti di tipo {type.__name__}')
            return func(*args, **kwargs)

        return wrapper

    return decorator

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        stop = datetime.datetime.now()
        elapsed = stop - start
        print(f'tempo impiegato: {elapsed}')
        return result
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print(f'la funzione "{func.__name__}" è stata chiamata')
        print(f'i suoi argomenti sono: {args}')
        print(f'i suoi argomenti posizionali sono: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@repeat(3)
def funzione(*args):
    print(f'mi hai dato {len(args)} argomenti!')

if __name__ == '__main__':
    funzione('a', 'b', 'c', 1)