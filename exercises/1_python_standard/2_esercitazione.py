"""
Esercizio 5
Scrivere una classe di base ClsBase in cui c'è un metodo addAttr che controlla se la classe ha l'attributo di nome s
e se tale attributo non è presente, allora aggiungere l'attributo s con un valore v; in caso contrario non fa niente.
 Il metodo deve funzionare anche per le eventuali sottoclassi agendo sulla sottoclasse senza bisogno però di essere
 ridefinito nella sottoclasse.
"""
class ClsBase:

    @classmethod
    def addAttr(cls, s, v):
        try:
            getattr(cls, s)
        except AttributeError:
            setattr(cls, s, v)

class ClsDer(ClsBase):
    pass

o = ClsBase()
ClsDer.addAttr("a1", "v1")
ClsDer.addAttr("a2", "v2")
o.addAttr("a2", "v3")
print(getattr(ClsDer, "a1"))
print(getattr(ClsDer, "a2"))
print(getattr(ClsBase, "a2"))

