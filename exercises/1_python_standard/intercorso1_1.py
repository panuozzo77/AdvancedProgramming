"""
- Scrivere una classe di base ClsBase in cui c’è un metodo addAttr che:
    - Prende in input due argomenti: una stringa s e un valore v
    - Controlla se la classe ha l’attributo di nome s e se tale attributo non è presente allora aggiunge alla classe
      l’attributo s con valore v; in caso contrario non fa niente
    - Il metodo deve funzionare anche per le eventuali sottoclassi di ClsBase
"""

class ClsBase:
    @classmethod
    def addAttr(cls, s, v):
        try:
            getattr(cls, s)
        except AttributeError:
            setattr(cls, s, v)