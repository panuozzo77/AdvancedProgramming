"""
- Scrivere nel file un decorator factory decFact(L1, L2) che prende in input una lista L1 di stringhe e una lista L2 di
  oggetti e produce un decoratore di classe che fa in modo che le istanze della classe nascano non solo con le variabili
  di istanza aggiunte al metodo __init__ della classe ma anche con le seguenti variabili di istanza:
  - per ogni i = 0, ... , len(L1) -1, una variabile con un nome uguale a L1[i] e valore uguale a L2[i]. Nel caso in cui
    il metodo __init__ della classe originaria aggiunge già una variabile di istanza con lo stesso nome di una di quelle
    aggiunte dal decoratore, allora il valore della variabile deve essere quello assegnato da __init__ della classe
    originaria.
"""


def decFact(L1: list, L2: list):
    def dec(cls):
        cls._oldinit = cls.__init__ # salvo il vecchio init

        def newinit(self, *args, **kwargs): # creo un nuovo init
            for n, v in zip(L1, L2): # scandisco contemporaneamente le liste
                setattr(cls, n, v) # aggiungo gli attributi alla classe
            cls._oldinit(self, *args, **kwargs) # eseguo il vecchio init per eventualmente sovrascrivere gli attributi ^

        setattr(cls, "__init__", newinit) # ridefinisco l'init della classe a questo qui nuovo
        return cls # restituisco la classe

    return dec