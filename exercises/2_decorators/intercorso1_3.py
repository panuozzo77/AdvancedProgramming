"""
- Scrivere un decorator factory decFact che restituisce un decoratore che dota la classe decorata di un metodo statico
  riportaVariabiliDiClasse che non prende in input alcun argomento.
  Il metodo restituisce un generatore di triple. Ciascuna tripla contiene come primo elemento il nome di una variabile
  di classe, come secondo elemento il valore della suddetta variabile e come terzo elemento la classe in cui viene
  trovata la variabile (potrebbe essere C o una delle sue superclassi)
"""

def decFact():
    def decorator(cls):
        @staticmethod
        def riportaVariabiliDiClasse():
            for classes in cls.mro():
                print("\nSono in ", classes)
                for k, v in classes.__dict__.items():
                    if not callable(v) and not k.startswith('__'):
                        t = (k, v, classes)
                        yield t

        setattr(cls, "riportaVariabiliDiClasse", riportaVariabiliDiClasse)
        return cls

    return decorator