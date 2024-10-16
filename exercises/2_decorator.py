"""
Scrivere il decoratore di funzione decora che trasforma la funzione decorata in una funzione che lancia l'eccezione TypeError
se uno o più argomenti non sono di tipo str. La funzione deve restituire una stringa formata dagli argomenti ricevuti in input e dal
risultato intervallati da uno spazio. Non dimenticate di convertire il risultato in stringa quando lo inserite nellaringa output.

Esempio: se la funzione riceve in input "il", "risultato", "è", la funzione non lancia l'eccezione e restituisce la stringa
"Il risultato è..." dove al posto dei puntini deve apparire il risultato della funzione
"""


def decora(f):
    def wrapper(*args, **kwargs):
            out=""
            for arg in list(args)+[v for k, v in kwargs.items()]:
                if type(arg)!=str:
                    raise TypeError
                out+=arg+" "
            result = str(f(*args, **kwargs))
            out+=result
            return out

        return wrapper

