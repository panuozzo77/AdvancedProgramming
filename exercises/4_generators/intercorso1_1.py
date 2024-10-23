"""
- Scrivere nel file una funzione generatrice generaQuadratoInput che prende come argomento un intero m>=1 e restituisce
  un iteratore dei quadrati degli interi via via digitati dall'utente fino a quando gli interi digitati sono minori o
  uguali di m. Più precisamente, se it è l'iteratore generato da generaQuadratoInput(m) allora ogni volta che viene digi
  tato next(it).
- Il programma si mette in attesa che l'utente digiti qualcosa (seguito da return) e se l'utente digita un intero minore
  o uguale di m allora next(it) restituisce il quadrato dell'intero digitato. Se invece:
        - l'intero digitato è maggiore di m,
        - o l'utente digita qualcosa che non è un intero
        - o interrompe l'esecuzione del programma,
 l'iteratore it smette di funzionare
"""

def generaQuadratoInput(m: int):
    while True:
        try:
            n = int(input("Digita un intero --> "))
            if n < m:
                yield n * n
            else:
                break
        except (KeyboardInterrupt, ValueError):
            print('Chiusura programma')
            break

if __name__ == "__main__":
    m = input('digita un intero che varrà come m --> ')
    for result in generaQuadratoInput(int(m)):
        print(f"Il quadrato è: {result}")