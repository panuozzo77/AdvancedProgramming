"""
- Scrivere una funzione che prende in input un intero positivo n e un valore sentinella
  e restituisce un generatore degli interi
- L’i-esimo elemento è (0+1+2+…+i-1). Se ad un certo punto raggiunge o supera il valore di sentinella
  allora l’iteratore smette di funzionare
"""

def sum_generator(n, flag):
    somma = 0
    for i in range(n):
        somma += i
        if i < flag:
            yield somma
        else:
            break

if __name__ == '__main__':
    n = int(input('inserisci un valore n: '))
    flag = int(input('inserisci un valore sentinella: '))
    for i in sum_generator(n, flag):
        print(i)