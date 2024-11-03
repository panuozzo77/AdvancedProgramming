"""
Scrivere un decorator factory che prende in input una classe ProxiedClass e restituisce un decorator di classe
myClassDecorator che prende in input una classe C e trasforma C in una classe Proxy della classe ProxiedClass.
Ogni volta che si invoca un metodo di istanza della classe decorata di fatto si invoca il metodo omonimo di ProxiedClass.
Si assuma che __init__ di ProxiedClass non riceva alcun argomento,eccezion fatta per self.
NON FARE ALCUNA ASSUNZIONE SU PROXIEDCLASS
"""

class ProxiedClass:
    def __init__(self):
        pass

    def test(self):
        print('test')

def decFact(ProxiedClass):
    def myClassDecorator(C):
        class Proxy(C):
            def __init__(self, *args, **kwargs):
                # Create an instance of ProxiedClass
                self._impl = ProxiedClass()
                super().__init__(*args, **kwargs)

            def __getattr__(self, name):
                # Forward method calls to the instance of ProxiedClass
                return getattr(self._impl, name)

        return Proxy
    return myClassDecorator

@decFact(ProxiedClass)
class C:
    pass

# Testing the proxy class
c = C()
c.test()  # Output: 'test'
