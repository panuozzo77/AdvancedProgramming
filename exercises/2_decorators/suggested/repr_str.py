'''
Task: Create a class decorator named @auto_repr_str that automatically adds __repr__ and __str__ methods to a class.
◦
Requirements:
The decorator should take the class as an argument and return a modified class

The generated __repr__ method should return a string representation of the object that includes the class name and the
values of all instance attributes. It could use introspection (like the inspect module if instance attributes can be
reliably determined this way, or simply iterate instance.__dict__.items()
) to find instance attributes. (Note: Using __dict__ for this is directly supported by the sources,
while using inspect for instance attributes might require going beyond the provided inspect examples).
 Let's stick to __dict__ which is mentioned in the context of instance attributes

The generated __str__ method can simply call the __repr__ method.
▪
If the class already defines __repr__ or __str__, the decorator should not overwrite them.
◦
Concepts Applied: Class decorators
, modifying class attributes (__repr__, __str__), instance attributes (__dict__), checking for existing methods.
'''


def auto_repr_str(cls):
    if '__repr__' not in cls.__dict__:
        def __repr__(self):
            class_name = self.__class__.__name__
            attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
            return f'metodo inserito con decoratore\n{class_name}({attrs})\n'

        setattr(cls, '__repr__', __repr__)

        # Aggiunge __str__ se non è già presente
    if '__str__' not in cls.__dict__:
        def __str__(self):
            return self.__repr__()

        setattr(cls, '__str__', __str__)

    return cls

@auto_repr_str
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

@auto_repr_str
class B:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # Personalizzato, quindi il decoratore non lo sovrascrive
        return f"B instance: {self.name}"

if __name__ == '__main__':
    a = A(10, 20)
    b = B("test")
    print(a)  # Output: A(x=10, y=20)
    print(b)  # Output: B instance: test