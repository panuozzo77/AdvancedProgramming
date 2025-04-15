      


def main():
    files=["file1","file2","file3","file4"]
    parole=["computer","very","with","it","algorithms"] 
    cerca(files,parole,4)
    


 

if __name__ == "__main__":
    main()

"""  Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):

La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file1 e` "computer".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file2 e` "very".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file4 e` "with".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare piu` della altre nel file file3 e` "algorithms".
"""

