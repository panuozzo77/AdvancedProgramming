	

		    
def main(): 
	searchers=[searcher('a','A',listCreator("ancora"),listCreator("Alto")),searcher('a','A',listCreator("alto"),listCreator("Ancora"))]

	
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
		
			
	
		
		


	
 
	
	for sel in searchers:
		sel.close()
	


if __name__ == "__main__":
    main()

"""
Il programma deve stampare:

Richiesta "fileNE" inviata al searcher 1:
Il file fileNE e` inesistente

Richiesta "fileNE" inviata al searcher 2:
Il file fileNE e` inesistente

Richiesta "fileI.txt" inviata al searcher 1:
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione']

Richiesta "fileI.txt" inviata al searcher 2:
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto']

Richiesta "fileII.txt" inviata al searcher  1:
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione', 'aurora']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione', 'aurora', 'assurdo']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione', 'aurora', 'assurdo', 'ancora']
Il searcher 1 non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole

Richiesta "fileII.txt" inviata al searcher  2:
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto', 'Aversa']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto', 'Aversa', 'Ancora']
Il searcher 2 non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole

"""
