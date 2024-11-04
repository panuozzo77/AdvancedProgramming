""""
Esercitazione Pre-Prova-Intercorso del 2024-11-04
Esercizio 1:
Scrivere un decorator factory che prende in input un oggetto
impl con valore di default None, una stringa name e restituisce un decoratore di
classe che  aggiunge alla classe decorata:
 - una variabile di classe substitute settata con impl
 - una proprieta` di nome name che il cui getter e setter si comportano come segue:
    - getter: se substitute è diverso da None allora il getter
      prende il valore dell'attributo da substitute altrimenti lo prende da self
    - setter: se  substitute è diverso da None allora il setter setta
      il valore dell'attributo dall'istanza a cui fa riferimento substitute altrimenti setta quello di self.
"""

#scrivere qui il codice dell'esercizio

def df(name: str, impl=None):
    def decClass(cls):
        cls.substitute = impl

        @property
        def prop(self):
            if cls.substitute is not None:
                return getattr(cls.substitute, name)
            else:
                return getattr(self, f"_{name}")

        @prop.setter
        def prop(self, value):
            if cls.substitute is not None:
                setattr(cls.substitute, name, value)
            else:
                setattr(self, f"_{name}", value)

        # Imposta la proprietà con il nome fornito
        setattr(cls, name, prop)

        return cls
    return decClass


class ForImpl:
    def __init__(self):
        self.a=10
        self.b=4

FI=ForImpl() #assegno a variabile per potervi accedere poi in test

@df("nameVar", FI)
class C:
    def __init__(self):
        self.nameVar=100

c=C()
print("ora stampo nameVar sia usando getter della property di c sia accedendo direttamente all'attributo di FI:", c.nameVar,FI.nameVar)
print("modifico nameVar con setter")
c.nameVar=50
print("ora stampo nameVar sia usando getter della property di c sia accedendo direttamente all'attributo di FI:", c.nameVar,FI.nameVar)

@df("nameOtherVar")
class D:
    def __init__(self):
        self.nameOtherVar=300

d=D()
print("ora stampo nameOtherVar  usando getter della property di d:", d.nameOtherVar)