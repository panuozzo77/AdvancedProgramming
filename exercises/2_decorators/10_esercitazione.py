"""
Esercitazione Pre-Prova-Intercorso del 2024-11-04
Esercizio 2 (gia` svolto)
Scrivere  il decoratore di funzione decf che fa in modo
che venga lanciata l'eccezione TypeError se il numero di argomenti è diverso da 2.
Altrimenti, se la funzione decorata restituisce un risultato questo viene aggiunto insieme al valore del
primo argomento in un file di nome risultato.txt.

Suggerimento: Ricordatevi di convertire a stringa il valore del primo argomento e il risultato quando li scrivete
nel file e di aprire il file in modo da non cancellare quanto scritto precedentemente nel file.
"""

def decf(function):
    def wrapper(*args, **kwargs):
        counter = 0
        counter += len(args) + len(kwargs)
        if len(args) != 2:
            raise TypeError("Function takes 2 arguments")
        else:
            fp = open('risultato.txt', 'a')
            result = function(*args, **kwargs)
            first_argument = None
            if len(args) == 1 and len(kwargs) == 1 or len(args) == 2:
                first_argument = args[0]
            if (len(kwargs) == 2):
                first_argument = kwargs[0]
            fp.write(f'{first_argument} {result}\n')
            fp.close()
            return result
    return wrapper

@decf
def somma(a, b):
    return a + b

somma(1, 2)