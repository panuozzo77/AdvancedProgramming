"""
Scrivere nel file un decorator factory DecoratorFactF che prende in input un valore v e restituisce un decoratore di
funzione che modifica il comportamento della funzione decorata come segue:
- se la funzione è invocata con tutti gli argomenti di tipo uguale a quello di v allora la funzione restituisce lo
  stesso valore che avrebbe restituito la funzione originaria;
- se uno o più argomenti sono di tipo diverso da quello di v allora la funzione restituisce il valore che la funzione
  originaria avrebbe restituito se fosse stata invocata solo su tutti gli argomenti dello stesso tipo di v;
- se la funzione originaria lancia un'eccezione, questa deve essere lanciata anche dalla funzione decorata.
"""