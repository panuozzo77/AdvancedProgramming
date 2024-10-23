"""
- Scrivere nel file esercizio1.py una funzione generatrice generaElementi che prende in input una lista L di elementi
  a due a due distinti e permette di ottenere un iteratore che scandisce gli elementi della lista nel seguente modo:
    - la prima volta che viene invocato next si ottiene il primo elemento della lista L[0]
    - per le invocazioni successive di next si ha il seguente comportamento:
        - sia L[i] l'elemento generato con l’invocazione di next
        - Se L[j] è un intero k diverso da j e compreso tra 1 e len(L)-1 allora la prossima invocazione di next
          restituisce L[k]
        - In caso contrario non vengono generati altri elementi e le invocazioni successive di next causano un'eccezione
    - Se L=[2, 8, 4, 'a', 3] allora le prime con le prime 4 invocazioni di next otteniamo 2 4 3 'a'
      mentre la quinta invocazione causa una StopIteration
"""

#Non è perfetto, teoricamente in automatico parte StopIteration
# ma chissà se va bene alla DeBonis
def generaElementi(li):
    yield li[0]
    el = li[0]
    while True:
        if isinstance(el, int) and 1 <= el <= len(li) - 1 and li[el] != el:
            yield li[el]
            el = li[el]
        else:
            break