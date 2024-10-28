"""
- scrivere nel file un decorator factory decFact che prende in input un tipo t e restituisce un decoratore di classe
  decorator che dota la classe decorata di un metodo di istanza 'addToList' che restituisce una lista contenente i nomi
  e i valori delle variabili di tipo t dell'istanza per cui è invocato. Ciascuna coppia (nome, valore) deve essere all'
  interno di una tupla. Il codice della classe non deve essere modificato.
"""
from pstats import add_callers


def decoratorFact(t):
    def decorator(cls):
        def addToList(self):
            L = []
            for k in self.__dict__.keys():
                if isinstance(self.__dict__[k], t):
                    L.append((k, self.__dict__[k]))
            return L
        setattr(cls, "addToList", addToList)
        return cls
    return decorator


@decoratorFact(int)
class classe1:
    def meth1(self):
        self.w1=dict({'dado':408, 'sei':9})
        #...