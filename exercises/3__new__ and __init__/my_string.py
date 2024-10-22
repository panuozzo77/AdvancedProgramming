"""
Ridefiniscimi il comportamento della classe Stringa (str) in questo modo:
- attraverso una sua classe figlia in cui, utilizzando __new__ ridefinisca il comportamento della classe String ottenendo la stringa in Uppercase
"""
class my_string(str):
    def __new__(cls, value):
            value = value.upper()
            # dico, prendimi chi sta sopra my_string ed utilizza il suo inizializzatore new con questo valore qua
            instance = super(my_string, cls).__new__(cls, value)
            return instance


val = my_string("ciao")
print(val)

"""
>>>CIAO
"""