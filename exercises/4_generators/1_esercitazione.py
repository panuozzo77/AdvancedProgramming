"""
Esercitazione Pre-Prova-Intercorso del 2024-11-04
Esercizio 4.
Scrivere una funzione generatrice generatore(L,X) che prende
in input una lista L di numeri  e una lista di interi X. Indichiamo con 'li'
l'i-esimo elemento di L e con 'xi' l'i-esimo elemento di X.
(ovvero gli elementi di indice i-1 delle due liste rispettivamente).

La funzione deve restituire un iteratore per il quale l'i-esima invocazione di next (con i<=lunghezza(X)),
si comporta come segue:
-   se 0 <= xi < lunghezza(L),  next restituisce il valore ottenuto sommando i primi xi valori di Li
-   se xi <0 oppure xi >=lunghezza(L), next restituisce l'eccezione IndexError.

"""
def somma(i, X):
    sum = 0
    for j in range(i):
        sum += X[j]
    return sum

def generatore(L, X):
    for i in range(len(X)):
        li = L[i]
        xi = X[i]
        if 0 <= xi <= len(L):
            yield somma(i, X)
        if xi < 0 or xi >= len(L):
            return

if __name__ == "__main__":
    l = [2, 10, 4, 3, 13, 21, 45, 55]
    print("I test: la lista passata come secondo argomento non genera eccezioni")
    for s in generatore(l, [4, 6, 1, 2, 5]):
        try:
            print(s, end=" ")
        except IndexError as e:
            print(e)

    print("\n\nII test: viene stampata la stringa con cui viene creata l'eccezione restituita dal generatore")
    for s in generatore(l, [4, 6, 1, 23, 5]):
        print(s, end=" ")

    print("\n\nIII test: viene catturata l'eccezione restituita dal generatore")
    for s in generatore(l, [4, 6, 1, 23, 5]):
        if (type(s) == IndexError):
            try:
                raise s
            except IndexError:
                print("Eccezione catturata!")
