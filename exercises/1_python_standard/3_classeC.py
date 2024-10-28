"""
- Scrivere una classe C per cui accade che ogni volta che si aggiunge una variabile di istanza ad una delle istanze di C
 in realtà la variabile viene aggiunta alla classe come variabile di classe.

Modificare la classe al punto precedente in modo tale che le istanze abbiano al più due variabili di istanza:
varA e varB e non deve essere possibile aggiungere altre variabili di istanza oltre a queste due. Se il programma avesse
bisogno di aggiungere altre variabili oltre a quelle sopra indicate, queste altre variabili verrebbero create come
variabili di classe e non di istanza.
"""

"""soluzione professoressa"""
class C:
    __slots__={"varA", "varB"}

    def __getattr__(self, nome):
        if nome in C.__slots__ : return super(C, self).__getattr__(nome)
        return getattr(C, nome)

    def __setattr__(self, nome, valore):
        if nome in C.__slots__ : return super(C, self).__setattr__(nome, valore)
        return setattr(C, nome, valore)



"""soluzione mia"""
class C:
    @classmethod
    def __setattr__(cls, key, value):
        setattr(cls, key, value)

class D:
    _numVars = 0

    def __setattr__(self, key, value):
        self.__class__._numVars += 1
        if self.__class__._numVars > 2:
            setattr(self.__class__, key, value)
        else:
            super().__setattr__(key, value)

c=C()
c2 = C()

c.varA=10
c.varB=20

print(c.varA,c.varB)
c.varE = 5
print(c.varE)
print(f'valore preso da c2: {c2.varA}')