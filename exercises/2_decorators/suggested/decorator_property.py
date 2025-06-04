def is_non_empty_str(value):
    return isinstance(value, str) and value.strip() != ""

def is_valid_isbn(value):
    return isinstance(value, str) and len(value.replace("-", "")) in (10, 13)

def is_in_range(min_val, max_val):
    return lambda x: isinstance(x, (int, float)) and min_val <= x <= max_val

'''
Questa versione ha un problema: ogni volta che viene chiamato sovrascrive l'init. Quindi non funziona come vorremmo
Abbiamo bisogno di accumulare prima tutte le variabili che necessitano di essere controllate
'''
def ensure_1(attr, condition):
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)

            value = getattr(self, attr)
            if not condition(value):
                raise ValueError(f'Valore errato per {attr!r} : {value!r}')

        cls.__init__ = new_init
        return cls

    return decorator

'''
Questa è la versione corretta
'''

def ensure(attr, condition):
    def class_decorator(cls):
        # Inizializza la lista dei validatori se non esiste
        if not hasattr(cls, "_validators"):
            cls._validators = []

            # Salviamo l'originale __init__ solo una volta
            original_init = cls.__init__

            def new_init(self, *args, **kwargs):
                # Prima chiamiamo l'originale
                original_init(self, *args, **kwargs)

                # Poi validiamo tutti gli attributi registrati
                for attr_name, cond in cls._validators:
                    value = getattr(self, attr_name)
                    if not cond(value):
                        raise ValueError(f"Invalid value for {attr_name}: {value}")

            cls.__init__ = new_init

        # Aggiungiamo questa nuova regola
        cls._validators.append((attr, condition))
        return cls
    return class_decorator

@ensure("title", is_non_empty_str)
@ensure("isbn", is_valid_isbn)
@ensure("price", is_in_range(1, 10000))
@ensure("quantity", is_in_range(0, 1000000))
class Book:
    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity

if __name__ == '__main__':
    b = Book("Il nome della rosa", "978-1234567890", 20, 3)
    print(b.value)  # OK
    print(b.__dict__)

    b = Book("", "invalid", -10, 3)
    print(b.value)  # OK
    # Lancerà ValueError: Invalid value for 'title': ''