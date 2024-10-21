"""Scrivere un decoratore di classe che, se applicato ad una classe, la modifica in modo che funzioni
come se fosse stata derivata dalla seguente classe base. N.B. le classi derivate da ClasseBase non
hanno bisogno di modificare i metodi f() e g() e la variabile varC. Inoltre quando vengono create le
istanze di una classe derivata queste ’’nascono’’ con lo stesso valore di varI settato da __init__ di
ClasseBase. """

class ClasseBase:
    varC=1000
    def __init__(self):
        self.varI=10
    def f(self,v):
        print(v*self.varI)

    @staticmethod
    def g(x):
        print(x*varC)