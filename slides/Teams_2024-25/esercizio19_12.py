""" Scrivere 
una coroutine searcher(c1,c2,receiver1, receiver2) che prende in input due caratteri c1 e c2
e due coroutine receiver1, receiver2 , e si comporta come segue:
ogni volta che riceve qualcosa verifica se questa e`
il nome di un file esistente e nel caso in cui lo sia cerca all’interno del file
le stringhe che cominciano con c1 e
quelle che cominciano con c2. 
Le prime vengono inviate a receiver1 mentre le seconde a receiver2.
Nel caso in cui non esista un file con quel nome,
la coroutine esegue solo la stampa della seguente stringa
"Il file {} e` inesistente", dove al posto delle parentesi
deve comparire il nome del file.
Scrivere inoltre una coroutine listCreator(stop) che ogni volta
che riceve una stringa la inserisce in una
lista (la lista e` una variabile locale alla coroutine) e
stampa la lista aggiornata con l’aggiunta della nuova parola.
I parametri receiver1 e receiver2 di searcher sono due coroutine listCreator.
Versione completa da 10: La couroutine listCreator(stop)  smette di
ricevere parole non appena riceve una parola uguale alla stringa stop
passata come argomento. Nell’implementazione della coroutine searcher occorre tenere conto del fatto che uno o entrambi
i receiver potrebbero non ricevere piu` le parole inviate.
Se ad un certo punto entrambi i receiver smettono di ricevere parole il searcher deve smettere anch’esso di ricevere stringhe.

Versione da al massimo 6 punti: la coroutine listCreator non fa niente altro rispetto a quanto sopra descritto (l’input stop viene ignorato).

Suggerimento: potete usare re.findall(r'\w+', testo) per estrarre parole da un testo.
"""

import functools
import re

	



 


		    
def main(): 
	lc_ancora=listCreator("ancora")
	lc_Alto=listCreator("Alto")
	lc_Ancora=listCreator("Ancora")
	lc_alto=listCreator("alto")
	searchers=[searcher('a','A',lc_ancora,lc_Alto),searcher('a','A',lc_alto,lc_Ancora)]


	
	for i,f in enumerate(searchers,start=1):
		print("Richiesta \"fileNE\" inviata al searcher {}:".format(i))
		f.send("fileNE")
		print()
		
	
	for i,f in enumerate(searchers,start=1):
		try:
			print("Richiesta \"fileI.txt\" inviata al searcher {}:".format(i))
			f.send("fileI.txt")
			print()
			
			
		except StopIteration:
			print("Il searcher {} non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole".format(i))
			print()
		
		
	
	for i,f in enumerate(searchers,start=1):
		try:
			print("Richiesta \"fileII.txt\" inviata al searcher  {}:".format(i))
			f.send("fileII.txt")
			print()
			
		except StopIteration:
			print("Il searcher {} non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole".format(i))
			print()
		
			
	
		
	for i,f in enumerate(searchers,start=1):
		try:
			print("Richiesta \"fileII.txt\" inviata al searcher  {}:".format(i))
			f.send("fileII.txt")
			print()
			
		except StopIteration:
			print("Il searcher {} non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole".format(i))
			print()

	


	
 
	
	for sel in searchers:
		sel.close()
	lc_alto.close()
	lc_Alto.close()
	lc_Ancora.close()
	lc_ancora.close()

if __name__ == "__main__":
    main()
