'''
Lo stato è condiviso nell'attributo _shared_state e tutte le istanze di Borg avranno lo stesso stato.

Lo stato di un'istanza è generalmente definito in __dict__.

In questo esempio, stiamo assegnando lo stesso dizionario a tutte le istanze della classe

__new__ viene usato per consentire a sottoclassi di tipi immutabili (str, int, tuple) di modificare
la creazione delle proprie istanze
'''

class Borg:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj