"""
Scrivere una funzione che prende in input un intero positivo ne restituisce e produce un generatore 'sommatoria'
degli interi  0, 1, 3, 6,10,... ovvero da 0 a n-1
"""


def sommatoria(n):
    somma = 0
    for i in range(n):
        somma += i
        yield somma




for i in sommatoria(6):
    print(i)