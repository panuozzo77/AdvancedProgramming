"""
- Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo statico che
  restituisce il numero di invocazioni del metodo passato come parametro al decorator factory
"""

def countdecfact(method):
    def dec(cls):
        cls._n = 0
        cls._oldmethod = getattr(cls, method)

        def newmethod(*args, **kwargs):
            cls._n += 1
            return cls._oldmethod(*args, **kwargs)

        @staticmethod
        def numInvocazioni():
            return cls._n

        setattr(cls, method, newmethod)
        setattr(cls, "numInvocazioni", numInvocazioni)

        return cls
    return dec