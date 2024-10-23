"""
- Scrivere una classe Impiegato e due sottoclassi Tecnico e Amministrativo.
- In aggiunta al metodo __init__, la classe Impiegato può avere solo un altro metodo, mentre le due sottoclassi possono
  avere solo __initi__
- Scrivere poi un programma che crei un certo numero di istanze delle tre classi e stampa il numero di: tecnici,
  amministratori e il totale di impiegati (può essere maggiore della somma di tecnici e amministratori, in quanto è
  possibile avere impiegati 'generici')
"""

import random


class Impiegato:
    ni = 0

    def __init__(self):
        Impiegato.ni += 1

    @staticmethod
    def count():
        return ("Sono stati creati {} elementi: {} impiegati, {} tecnici e {} amministratori").format(Impiegato.ni + Tecnico.nt + Amministrativo.na, Impiegato.ni, Tecnico.nt, Amministrativo.na)


class Tecnico(Impiegato):
    nt = 0

    def __init__(self):
        Impiegato.__init__(self)
        Tecnico.nt += 1


class Amministrativo(Impiegato):
    na = 0

    def __init__(self):
        Impiegato.__init__(self)
        Amministrativo.na += 1


l = list()
for _ in range(10):
    r = random.randint(1, 3)
    if r == 1:
        l.append(Impiegato())
    elif r == 2:
        l.append(Tecnico())
    else:
        l.append(Amministrativo())

print(Impiegato.count())