"""
Esercitazione Pre-Prova-Intercorso del 2024-11-04
Esercizio 3
Scrivere un decorator factory decFact  che ha come argomento un intero n e produce un decoratore di classe
che dota la classe decorata di un decoratore di funzione simile a quello definito al punto 3 ma che,
a differenza di quel decoratore, fa in modo che l'eccezione venga lanciata se
il numero di argomenti è diverso da n.

Suggerimento: Ricordatevi che il decoratore di funzione può essere trattato
come una funzione qualsiasi e â€œattaccatoâ€
alla classe decorata così come abbiamo più volte visto durante le lezioni.
"""

def decFact(n : int):
    def decClass(cls):

        def decf(function):
            def wrapper(*args, **kwargs):
                counter = 0
                counter += len(args) + len(kwargs)
                if counter != n:
                    raise TypeError(f"Function takes {n} arguments")
                return function(*args, **kwargs)

        setattr(cls,"decf", decf)

        return cls
    return decClass

@decFact(3)
class NewClass1:
        pass


@decFact(0)
class NewClass2:
        pass



def f(*args,**kwargs):
        return "io sono il risultato della funzione invocata con args={} e kwargs={}\n".format(args,kwargs)



g=NewClass1.decf(f)

print("invoco g(1,2,3,4)")
try:
        g(1,2,3,4)
except TypeError:
        print("g e` stata invocata con un numero di argomenti diverso da tre")
print("\ninvoco g()")
try:
        g()
except TypeError:
        print("g e` stata invocata con un numero di argomenti diverso da tre")
print("\ninvoco g(3,2,k=5,f=6)")
try:
        g(3,2,k=5,f=6)
except TypeError:
        print("g e` stata invocata con un numero di argomenti diverso da tre")

print("\ninvoco g(1,2,3)")
try:
    g(1,2,3)
except TypeError:
    pass
print("\ninvoco g(x=2,j=6,k=3)")
try:
    g(x=2,j=6,k=3)
except TypeError:
    print('eccezione!')


h=NewClass2.decf(f)



try:
        h(1,2,3,4)
except TypeError:
        print("\n\nh e` stata invocata con un numero di argomenti diverso da zero")
print("\ninvoco h(a=4,b=3,c=7)")
try:
        h(a=4,b=3,c=7)
except TypeError:
        print("h e` stata invocata un numero di argomenti diverso da zero")
print("\ninvoco h(3,2,k=5,f=6)")
try:
        h(2,k=5,f=6)
except TypeError:
        print("h e` stata invocata un numero di argomenti diverso da zero")

print("\ninvoco h()")
try:
    h()
except TypeError:
    print("h e` stata invocata un numero di argomenti diverso da zero")
