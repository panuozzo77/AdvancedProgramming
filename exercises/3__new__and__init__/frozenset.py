"""
Scrivere nel file la classe MySet che estende frozenset in modo tale che quando si crea l'istanza di MySet, l'istanza
creata contenga solo gli elementi di tipo int dell'oggetto iterabile passato come argomento a MySet(). Se MySet() non
prende input niente, l'istanza creata è vuota.
"""

class MySet(frozenset):
    def __new__(cls, iterable = None):
        if iterable is None:
            iterable = []
        filtered = (x for x in iterable if isinstance(x, int))
        obj = super().__new__(cls, filtered)
        return obj

if __name__ == '__main__':
    vocali = ['a', 'e', 'i', 'o', 'u', 1]
    a = MySet(vocali)
    print(a)

'''
__new__ è usato perché frozenset è immutabile: l’oggetto va costruito al momento della chiamata a __new__.

frozenset accetta un solo argomento iterabile nel suo costruttore. 
Passare *args e poi chiamare super().__new__(arg_appoggio) non funziona come previsto.

Stai trattando args come se potessero essere più input, ma la classe dovrebbe accettare 
al massimo un iterabile, come MySet([1, 2, 'a']).

Non serve gestire kwargs, perché frozenset non li usa.
'''