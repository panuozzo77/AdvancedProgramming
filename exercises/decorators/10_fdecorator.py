"""
Modificare la funzione al punto precedente in modo che la funzione decorata operi su qualsiasi elemento possa essere
convertito in int e che non si abbia errore se un elemento della lista non può essere convertito in int anche se è di un tipo
convertibile a int (ad esempio "anna")
"""
import functools
from curses import wrapper

from PyQt5.QtSql import password

import functools


def fdecorator(funz):
    @functools.wraps(funz)
    def wrapper(lst, *args, **kwargs):
        def conv(a):
            try:
                return int(a)
            except Exception:
                return None  # Return None explicitly if conversion fails

        # Convert the list and filter out None values
        args = [conv(x) for x in lst if conv(x) is not None]
        return funz(*args, **kwargs)

    return wrapper


