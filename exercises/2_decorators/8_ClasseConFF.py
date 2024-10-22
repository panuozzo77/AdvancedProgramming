"""
Scrivere un decorator factory che prende in input una classe ClasseConFF e due stringhe funz e ff e restituisce un
decoratore di classe che decora una classe in modo tale che se viene invocata funz di fatto al posto di funz viene
invocata la funzione ff della classe ClasseConFF
"""

def decoratorFactory(cls,funz="funz",ff="ff"):
    temp = getattr(cls, funz)
    # funz = ff
    setattr(cls,funz, getattr(cls,ff))
    # ff = funz
    setattr(cls,ff,temp)

    return cls

@decoratorFactory
class ClasseConFF():
    def funz(self):
        print("Invocato funz")

    def ff(self):
        print("Invocato ff")

c=ClasseConFF()
print('sto invocando funz')
c.funz()
print('\n')
print('sto invocando ff')
c.ff()

"""
Il programma stampa:
sto invocando funz

sto invocando ff
"""