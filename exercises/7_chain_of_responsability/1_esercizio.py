"""
- Scrivere una funzione che prende in input una sequenza di richieste (liste di 2 interi) e passa ciascuna richiesta ad
  una catena di gestori ciascuno dei quali è una coroutine.
- Se il primo intero della lista è nell'intervallo [0, 4] allora la richiesta viene gestita da Handler_04 che stampa
  "Richiesta {} gestita da Handler_04.
- Se il primo intero nella lista è nell'intervallo [5, 9] allora la richiesta viene gestita da Handler_59 che
  "Richiesta {} gestita da Handler_59.
- Se il primo intero della lista è maggiore di 9 allora la richiesta viene gestita da Handler_gt9 che stampa:
  "Messaggio da Handler_gt9: non è stato possibile gestire la richiesta {}. Richiesta modificata".
    - Dopo aver effettuato la stampa, Handler_gt9 sottrae al primo intero della lista il secondo intero della lista e lo
      invia nuovamente ad una nuova catena di gestori.
- Se la richiesta non è una lista di 2 numeri o il primo intero della lista è minore di 0 la richiesta viene gestita da
  Default_Handler che stampa semplicemente
  "Richiesta {} gestita da Default_Handler: non è stato possibile gestire la richiesta"
- Nelle suddette stampe, la lista nella richiesta deve comparire al posto delle parentesi graffe
"""

import functools


# Decoratore per trasformare una funzione in una coroutine
def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)  # Avanza al primo yield
        return generator

    return wrapper


@coroutine
def default_handler():
    while True:
        request = (yield)
        print(f"Richiesta {request} gestita da Default_Handler: non è stato possibile gestire la richiesta")


@coroutine
def handler_04(successor):
    while True:
        request = (yield)
        if 0 <= request[0] <= 4:
            print(f"Richiesta {request} gestita da Handler_04.")
        else:
            successor.send(request)


@coroutine
def handler_59(successor):
    while True:
        request = (yield)
        if 5 <= request[0] <= 9:
            print(f"Richiesta {request} gestita da Handler_59.")
        else:
            successor.send(request)


@coroutine
def handler_gt9(successor):
    while True:
        request = (yield)
        if request[0] > 9:
            print(
                f"Messaggio da Handler_gt9: non è stato possibile gestire la richiesta {request}. Richiesta modificata")
            modified_request = [request[0] - request[1], request[1]]
            successor.send(modified_request)
        else:
            successor.send(request)


def process_requests(requests):
    # Creazione della catena di gestori
    chain = handler_04(handler_59(handler_gt9(default_handler())))

    for request in requests:
        if isinstance(request, list) and len(request) == 2 and all(isinstance(i, int) for i in request):
            chain.send(request)
        else:
            default_handler_instance = default_handler()
            default_handler_instance.send(request)


# Esempio di utilizzo
requests = [
    [3, 1],
    [7, 2],
    [11, 5],
    [15, 3],
    [8, 4],
    [-1, 0],
    [4.5, 2],  # Non valido
]

process_requests(requests)
