"""
Scrivere nel file esercizio1.py una funzione generatrice generaElementi che prende in input una lista L di elementi a
due a 2 distinti (Non c'è bisogno di controllare che siano distinti). Scandisce la lista nel seguente modo:
- la prima volta che viene invocato next si ottiene il primo elemento della lista L[0]
- per le invocazioni successive di next si ha il seguente comportamento:
    - sia L[j] l'elemento generato con la più recente invocazione di next. Se L[j] è un intero k diverso da j e compreso
      tra 1 e len(L)-1 allora la prossima invocazione di next restituisce L[k]. In caso contrario non vengano generati
      altri elementi e le invocazioni successive di next causano un'eccezione.

  ES: L=[2, 8, 4, 'a', 3] allora le prime con le prime 4 invocazioni di next otteniamo 2 4 3 'a' mentre la quinta
  invovcazione causa StopIteration
"""

def generaElementi(L):
    j = 0
    if j == 0:
        yield L[j]
    while True:
        k = L[j]  # Prende l'elemento corrente
        if isinstance(k, int) and k != j and 1 <= k < len(L):
            j = k  # Aggiorna j all'indice k
            yield L[j]  # Restituisce l'elemento in L[k]
        else:
            #raise StopIteration  # Altrimenti, termina la generazione
            break
if __name__ == '__main__':
    # L = [2, 8, 4, 'a', 3]
    L = [2, 8, 6, 'a', 4, 1, 3]
    try:
        for i in generaElementi(L):
            print(i)
    except StopIteration:
        print("Eccezione Presa")

