class Mediated:
    def __init__(self):
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)

'''
Questo è un decoratore di classe ANALOGO che fa la stessa cosa della classe

Dota la classe di un attributo di classe 'mediator'

Il metodo on_change chiama lo stesso metodo ma sull'istanza del mediator, se esiste
'''
def mediated(Class):
    setattr(Class, 'mediator', None)

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)

    setattr(Class, "on_change", on_change)
    return Class

'''
Così possiamo 'estendere' la classe in entrambi i modi:
'''
class new(Mediated):

@mediated
class New:
    pass