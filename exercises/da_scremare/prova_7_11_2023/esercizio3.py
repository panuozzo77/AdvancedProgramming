'''
Scrivere nel file esercizio3.py la classe MySet che estende frozenset in modo tale che quando si
crea un’istanza di MySet, l’istanza di MySet creata contenga solo gli elementi di tipo int
dell’oggetto iterabile passato come argomento a MySet(). Se MySet() non prende input niente
allora l’istanza creata è vuota.
'''
class MySet(frozenset):
    def __new__(cls, iterable=None):
        if iterable is None:
            return super().__new__(cls, frozenset())
        else:
            # Filter the iterable to include only int elements
            filtered_iterable = (item for item in iterable if isinstance(item, int))
            return super().__new__(cls, frozenset(filtered_iterable))

S=MySet([])
print('S=',S)

S=MySet((1,"a","bcd",4,{},9,4.5))
print('S=' ,S)
