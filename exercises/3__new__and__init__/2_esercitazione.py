"""
Esercitazione Pre-Prova-Intercorso del 2024-11-04
esercizio 5
Scrivere nel file esercizio3.py, all'interno della classe C, due classi Gemella1 e Gemella2 nessuna delle quali è
derivata dall'altra. Le istanze di ciascuna classe devono essere tra di loro identiche e anche identiche alle istanze
dell'altra classe (identiche vuol dire stessi attributi).

Scrivere poi sempre nello stesso file la classe Derivata che ha come classe base Gemella1. Le istanze di Derivata
sono tra di loro identiche ma non condividono lo stesso stato di quelle di Gemella1 e Gemella2.
Non occorre scrivere il codice per fare altro oltre a quanto richiesto.
"""

class C:
    shared_state = {}

    class Gemella1:
        def __new__(cls, *args, **kwargs):
            o = super(C.Gemella1, cls).__new__(cls, *args, **kwargs)
            o.__dict__ = C.shared_state
            return o

    class Gemella2:
        def __new__(cls, *args, **kwargs):
            o = super(C.Gemella2, cls).__new__(cls, *args, **kwargs)
            o.__dict__ = C.shared_state
            return o

class Derivata(C.Gemella1):
    _dict = {}

    def __new__(cls, *args, **kwargs):
        o = super(C.Gemella1, C.Gemella1).__new__(cls)
        o.__dict__ = cls._dict
        return o


t1=C.Gemella1()
t2=C.Gemella2()
t1.x=4
print("La variabile x di t2 ha valore {}.".format(t2.x))
del(t2.x)
try:
    print(t1.x)
except AttributeError:
    print("L'attributo x e` stato cancellato")
t1.x1="maria"
t2.x2="piera"
def f(self): print ("Sono la funzione f di Gemella1 e questi sono gli attributi dell'istanza {}:{}.".format(id(self),self.__dict__))
C.Gemella1.f= f
def f(self): print ("Sono la funzione f di Gemella2 e questi sono gli attributi dell'istanza {}: {}.".format(id(self),self.__dict__))
C.Gemella2.f= f
C.Gemella1.f(t1)
C.Gemella2.f(t2)

print("\nTesto Derivata")
d=Derivata()
e=Derivata()
e.x1=10
d.x2=20
d.x="saluti"
C.Gemella1.f(t1)
C.Gemella2.f(t2)
Derivata.f(d)
Derivata.f(e)


"""
I programmi devonno stampare:
=================esercizio 1=============
ora stampo nameVar sia usando getter della property di c sia accedendo direttamente all'attributo di FI: 100 100
modifico nameVar con setter
ora stampo nameVar sia usando getter della property di c sia accedendo direttamente all'attributo di FI: 50 50
ora stampo nameOtherVar  usando getter della property di d: 300
+++++++++++++esercizio 2-3+++++++++++
invoco g(1,2,3,4)
g e` stata invocata con un numero di argomenti diverso da tre

invoco g()
g e` stata invocata con un numero di argomenti diverso da tre

invoco g(3,2,k=5,f=6)
g e` stata invocata con un numero di argomenti diverso da tre

invoco g(1,2,3)

invoco g(x=2,j=6,k=3)


h e` stata invocata con un numero di argomenti diverso da zero

invoco h(a=4,b=3,c=7)
h e` stata invocata un numero di argomenti diverso da zero

invoco h(3,2,k=5,f=6)
h e` stata invocata un numero di argomenti diverso da zero

invoco h()
+++++++++++++esercizio 4+++++++++++
I test: la lista passata come secondo argomento non genera eccezioni
19 53 2 12 32 

II test: viene stampata la stringa con cui viene creata l'eccezione restituita dal generatore
19 53 2 Indice errato 32 

III test: viene catturata l'eccezione restituita dal generatore
Eccezione catturata!
"""
