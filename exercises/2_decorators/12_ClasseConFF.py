"""
Scrivere un decorator factory che prende in input una classe ClasseConFF e due stringhe funz e ff e restituisce un
decoratore di classe che decora una classe in modo tale che se viene invocata funz di fatto al posto di funz viene
invocata la funzione ff della classe ClasseConFF
"""


class ClasseConFF:
    def ff(self):
        print("sono ff")


@decFact(ClasseConFF, "f", "ff")
class Classe1:
    @staticmethod
    def aggiungiFunzione(funzione=None):
        if funzione is not None:
            Classe1.f = funzione


if __name__ == "__main__":
    istanza2 = Classe1()
    Classe1.aggiungiFunzione()
    istanza2.f()
    Classe1.aggiungiFunzione(lambda self: print("sono f"))
    istanza3 = Classe1()
    istanza3.f()

"""
Il programma stampa:
sono ff
sono f
"""