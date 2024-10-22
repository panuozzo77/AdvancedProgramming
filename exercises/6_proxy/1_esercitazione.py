"""
Scrivere una classe MyProxy che è il proxy della classe MyClass. Ogni volta che viene invocato un metodo di istanza
della classe MyProxy, di fatto viene invocato l'omonimo metodo di istanza di MyClass. Non deve essere usata l'ereditarietà

- si assuma che __init__ di MyClass prenda in input un argomento x e che il comportamento dei suoi metodi di istanza
dipenda dal valore di x passati a __init__
"""

class myClass:
    def __init__(self, x):
        self.value = x
        print(f'my variable is a {type(self.value)} with value: {self.value}')

    def add10(self):
        self.value += 10
        print('I added 10!')

    def add_string(self):
        self.value += " Hello World!"

    def print_value(self):
        print(f'actual value: {self.value}')

class Proxy:
    def __init__(self, x):
        self.__implementation = myClass(x)

    def __getattr__(self, name):
        return getattr(self.__implementation, name)

o = Proxy(5)
o.add10()
o.print_value()