'''
Task: Create a class decorator named @readonly_after_init that, when applied to a class,
      makes all instance attributes read-only after the __init__ method finishes executing.

Requirements:
The decorator should take the class as an argument and return a modified class
It should wrap the original __init__ method. Inside the wrapper, after calling the original __init__,
it should replace the instance's __setattr__ method with a custom one that raises an
AttributeError if anyone tries to set or modify an attribute

The original __setattr__ should still be available within the wrapper's __init__ phase to allow attributes to be set initially.
◦
Concepts Applied: Class decorators
, wrapping methods (__init__), dynamic attribute assignment/modification (__setattr__), accessing original methods (e.g., storing the original __setattr__).
'''

def readonly_after_init(cls):
    old_init = cls.__init__

    def new_setattr(self, name, value):
        raise AttributeError('Gli attributi non sono modificabili a run-time!')

    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.__setattr__ = new_setattr

    cls.__init__ = new_init

    return cls

@readonly_after_init
class A:
    def __init__(self, attributo, **kwargs):
        self.attributo = attributo

        for name, arg in kwargs.items():
            self.name = arg


if __name__ == '__main__':
    classe = A(attributo=10, a=1, b=2)
    print(classe.attributo)
    classe.a = 3
    classe.attributo = 3

