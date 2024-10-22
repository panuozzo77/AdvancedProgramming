"""
- Scrivere una classe C per cui accade che ogni volta che si aggiunge una variabile di istanza ad una delle istanze di C
 in realtà la variabile viene aggiunta alla classe come variabile di classe.

Modificare la classe al punto precedente in modo tale che le istanze abbiano al più due variabili di istanza:
varA e varB e non deve essere possibile aggiungere altre variabili di istanza oltre a queste due. Se il programma avesse
bisogno di aggiungere altre variabili oltre a quelle sopra indicate, queste altre variabili verrebbero create come
variabili di classe e non di istanza.
"""


class C:

    __slots__=['varA','varB']

    def __init__(self):
        self.varA='varA'
        self.varB='varB'

    def __setattr__(self, key,value):
        # Se l'attributo non esiste già come variabile di classe
        if not hasattr(self.__class__, key):
            # Crea una variabile di classe
            setattr(self.__class__, key, value)
        else:
            # Altrimenti, usa il comportamento normale
            super().__setattr__(key, value)

c=C()
c2 = C()

c.varA=10
c.varB=20

print(c.varA,c.varB)
c.varE = 5
print(c.varE)
print(f'valore preso da c2: {c2.varA}')
# print(c.__dict__)