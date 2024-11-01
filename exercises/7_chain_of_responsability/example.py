from abc import ABC, abstractmethod


class Handler(ABC):
    def handle(self, data: str):
        raise NotImplementedError

class Chain:
    def add_handler(self, handler):
        self._handlers.append(handler)

    def __init__(self, *handlers):
        self._handlers = []
        if handlers:
            for handler in handlers:
                Chain.add_handler(self, handler)

    def handle(self, data):
        for handler in self._handlers:
            data = handler.handle(data)
        return data

class H1(Handler):
    def handle(self, data):
        print(f"input: {data}")
        return data

class H2(Handler):
    def handle(self, data):
        print(f"reversed: {data[::-1]}")
        return data

class H3(Handler):
    def handle(self, data):
        print(f"n. lettere: {len(data)}")
        return data

"divisore"

class FatherHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, data):
        if self._successor is not None:
            self._successor.handle(data)

class FH1(FatherHandler):
    def handle(self, data):
        if data:
            print(f"input: {data}")
            super().handle(data)

class FH2(FatherHandler):
    def handle(self, data):
        if isinstance(data, str):
            print(f"reversed: {data[::-1]}")
            super().handle(data)

class FH3(FatherHandler):
    def handle(self, data):
        if isinstance(data, str):
            print(f"n. lettere: {len(data)}")
            super().handle(data)

if __name__ == '__main__':
    "un primo approccio, verrebbe una cosa del genere, senza studiarlo dall De Bonis"
    # chain = Chain(H1(), H2(), H3())
    # output = chain.handle("messaggio")
    # print(f"\noutput dopo gli handlers: {output}")
    "seguendo la teoria della De Bonis, invece:"
    chain = FH1(FH2(FH3()))
    chain.handle("messaggio")