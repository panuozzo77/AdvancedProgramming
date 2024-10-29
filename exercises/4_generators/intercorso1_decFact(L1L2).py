"""
Scrivere nel file esercizio3.py un decorator factory decFact(L1,L2) che prende in input una lista di stringhe e una
stringa di oggetti e produce un decoratore di classe che fa in modo che le istanze della classe nascano non solo con le
variabili di istanza aggiunte dal metodo __init__ della classe ma anche con le seguenti variabili di istanza:
    - per ogni i = 1... len(1) una variabile con nome uguale a quello della i-esima stringa di L1 e valore uguale
      all'i-esimo oggetto di L2. Nel caso in cui __init__ della classe originaria aggiungeva già una variabile di
      istanza con nome uguale all'i-esima stringa di L1 allora il valore della variabile deve essere quello assegnato da
      __init__ della classe originaria.
"""
# L1 stringhe, L2 oggetti
def decFact(L1, L2):
    def decorator(cls):
        # Salviamo il metodo __init__ originale
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            # Chiamiamo il __init__ originale
            original_init(self, *args, **kwargs)

            # Aggiungiamo le variabili di istanza da L1 e L2
            for name, value in zip(L1, L2):
                if not hasattr(self, name):  # Controlla se la variabile esiste già
                    setattr(self, name, value)

        # Sostituiamo il __init__ della classe con il nuovo __init__
        cls.__init__ = new_init
        return cls
    return decorator

# Esempio
@decFact(['var1', 'var2'], [10, 20])
class MyClass:
    def __init__(self):
        self.var1 = 5  # Questa variabile sarà mantenuta


if __name__ == '__main__':
    obj = MyClass()
    print(obj.var1)  # Output: 5 (da __init__)
    print(obj.var2)  # Output: 20 (da decFact)



