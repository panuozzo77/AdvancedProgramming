class ClasseBase:
    varC = 1000
    def __init__(self):
        self.varl = 10

    def f(self, v):
        print(v*self.varl)

    @staticmethod
    def g(x):
        print(x * ClasseBase.varC)


def classDecorator(cls):
    varC = ClasseBase.varC

    def new_init(self):
        self.varl = 10

    cls.__init__ = ClasseBase.__init__

    setattr(cls, 'f', ClasseBase.f)
    setattr(cls, 'g', ClasseBase.g)
    return cls

@classDecorator
class Ext:
    pass

if __name__ == '__main__':
    t = Ext()
    print(t.__dict__)
    t.f(10)
    Ext.g(2)