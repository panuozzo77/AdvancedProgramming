"""
Scrivere due classi Twin1 e Twin2 nessuna delle quali è derivata dell'altra. Le istanze di ciascuna classe devono
essere identiche e anche identiche alle istanze dell'altra classe (identiche vuol dire con stessi attributi). Non occorre
scrivere il codice per fare altro oltre a quanto richiesto
"""

"""
Soluzione proposta dalla professoressa:
"""

class Top:
    _shared= {}

    class Twin1 :
        def __new__(cls, *args, **kwargs):
            o = super(Top.Twin1, cls).__new__(cls, *args, **kwargs)
            o.__dict__ = Top._shared
            return o

    class Twin2 :
        def __new__(cls, *args, **kwargs):
            o = super(Top.Twin2, cls).__new__(cls, *args, **kwargs)
            o.__dict__ = Top._shared
            return o

class Der1(Top.Twin1):
    _shared = {}
    def __new__(cls, *args, **kwargs):
        o = super(Top.Twin1, Top.Twin1).__new__(cls, *args, **kwargs)
        o.__dict__ = Der1._shared
        return o

if __name__ == '__main__':
    # test()
    t1 = Top.Twin1()
    t2 = Top.Twin2()
    t1.x = 4
    print(f'la variabile x di t2 ha valore {t2.x}')
    del(t2.x)
    try:
        print(t1.x)
    except AttributeError:
        print("L'attributo è stato cancellato")
    t1.x1 = "maria"
    t2.x2 = "piera"

"""
Mio tentativo
"""

dizionario = {}

class Twin1:

    def __init__(self, **kwargs):
        dizionario.update(kwargs)
        self.__dict__= dizionario

    def __eq__(self, other):
        return isinstance(other, Twin2) and self.__dict__ == other.__dict__

    def __setattr__(self, key, value):
        dizionario[key] = value

    def __getattr__(self, item):
        return dizionario[item]


class Twin2:

    def __init__(self, **kwargs):
        dizionario.update(kwargs)
        self.__dict__ = dizionario

    def __eq__(self, other):
        return isinstance(other, Twin2) and self.__dict__ == other.__dict__

    def __setattr__(self, key, value):
        dizionario[key] = value

    def __getattr__(self, item):
        return dizionario[item]


# Funzione per verificare l'identità delle istanze
def are_identical(twin1_instance, twin2_instance):
    return twin1_instance == twin2_instance and twin1_instance.__dict__ == twin2_instance.__dict__

t1 = Twin1()
t2 = Twin2()
t1_1 = Twin1()

t1.a = 5
t1.b = 2

def test():
    print(t2.a)
    print(f'are Twin1 and Twin2 the same: {are_identical(t1, t2)}')
    print(f'are Twin1 and Twin1_1 the same: {are_identical(t1, t1_1)}')
    print(t1_1.a)





