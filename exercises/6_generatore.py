"""Scrivere un generatore che ogni volta che è invocato stampa un elemento dalla lista e smette di stampare elementi
non appena incontra un elemento maggiore di 10"""

class Test():
    L = [1, 3, 7, 10, 12]
    def __init__(self):
        pass

    def generator(self):
        for i in self.L:
            if i < 10:
                yield i
            else:
                # raise FoundTen
                yield "10 rilevato!"

    def printer(self):
        print(self.L, self.L[2])

if __name__ == '__main__':
    x = Test()
    i = 1
    for num in x.generator():
        print(f"iterazione n°{i}: restituito: {num}")
        i += 1
