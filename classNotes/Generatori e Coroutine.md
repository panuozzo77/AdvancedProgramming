# Generatori e Coroutine

- L’uso di yield in un corpo di una funzione trasforma la funzione in generatore.
- Quando viene invocata una funzione generatore viene restituito un iteratore chiamato generatore.
- L’esecuzione del generatore comincia quando viene invocato uno dei metodi del generatore. L’esecuzione continua fino alla prima espressione di yield dove l’esecuzione è sospesa e viene restituito il valore prodotto da yield al codice che ha invocato il metodo.
- Quando l’esecuzione è ripresa invocando uno dei metodi del generatore, l’espressione yield assume un valore che dipende dal metodo che ha fatto riprendere l’esecuzione. Se viene usato __next__() allora il valore dell’espressione yield è None.
    - Se l’esecuzione del generatore termina senza produrre risultato allora lancia StopIteration.
    - altrimenti se viene usata send(), riprende l’esecuzione del generatore ed invia un valore al generatore. Il valore passato è il risultato dell’espressione yield da cui riprende l’esecuzione.
    - quando send() è invocata per avviare il generatore, deve contenere None come argomento perché non è stata ancora raggiunta l’espressione yield che riceve il valore.
    
    ```python
    def raddoppio():
    	while True:
    		x = yield
    		print("Stampa tra un yield e l'altro del corpo del while x=",x)
    		x = yield x * 2
    		print("stampa fine corpo while x="x)
    ```
    
    ```python
    g=raddoppio()
    r=next(g) #è stata raggiunta la linea 3, inseriamo None (il primo risultato) restituito da yield in r
    if r==None:
    	print("next(g) non ha restituito nulla")
    r=g.send(5) #riprendiamo l'esecuzione da riga 3, in x viene messo 5, in r restituiamo 10
    print("send ha restituito:",r)
    
    r=next(g) #riprendiamo da 5, non abbiamo passato nulla, quindi in x in riga 3 mette None e restituisce None
    if r==None:
    	print("next(g) non ha restituito nulla")
    r=g.send(8) #riprendiamo esecuzione da 3, in x è messo 8, restituisce 16
    print("send ha restituito:",r)
    
    >>>next(g) non ha restituito niente
    >>>stampa tra un yield e l'altro del corpo del while: x ha valore x= 5
    >>>send ha restituito 10
    >>>stampa fine corpo while. x= None
    >>>next(g) non ha restituito niente
    >>>stampa tra un yield e l'altro del corpo del while: x ha valore 8
    >>>send ha restituito 16
    ```
    
    ```python
    print("un'altra versione di raddoppio")
    def raddoppio():
    	x=2 #occorre inizializzare x perche’ altrimenN errore alla prima esecuzione dell'istruzione contenente yield
    	
    	while True:
    		x=(yield x) *2
    		print("stampa tra un yield e l'altro del corpo del while: x ha valore",x)
    
    g=raddoppio()
    r=next(g)
    print("next(g) ha resNtuito il {} prodoSo dalla prima esecuzione di yield’’.format( r ))
    r=g.send(5)
    print ("send ha resNtuito ",r)
    r=g.send(8)
    print ("send ha resNtuito ",r)
    
    >>>un' altra versione di raddoppio
    >>>next(g) ha resNtuito il 2 prodoSo dalla prima esecuzione di yield
    >>>stampa tra un yield e l'altro del corpo del while: x ha valore 10
    >>>send ha resNtuito 10
    >>>stampa tra un yield e l'altro del corpo del while: x ha valore 16
    >>>send ha resNtuito 16
    ```
    

### Metodi del Generatore

- throw() lancia un’eccezione del tipo passato in argomento nel punto in cui l’esecuzione del generatore è stata sospesa.
    - restituisce il prossimo valore prodotto dal generatore se questo ne produce uno nuovo.
    - Se il generatore non cattura l’eccezione ‘inviata’ da throw o lancia un’eccezione differente, allora l’eccezione immessa da throw si propaga al codice che ha invocato throw
- close() lanci una GeneratorExit nel punto dove è sospesa.
    - Se accade che il generatore termini subito dopo senza lanciare eccezioni, o se è già chiuso, o se lancia GeneratorExit, close restituisce il controllo al codice che l’ha invocato
    - Se il generatore produce un valore, viene lanciata RuntimeError. Se lancia un’eccezione viene propagata al codice che ha invocato close.
    - close() non fa nulla se il generatore ha già terminato l’esecuzione
    
    ```python
    def echo(value=None):
    	def echo(value=None):
    	try:
    		while True:
    			try:
    				value = ( yield value)
    			except Exception as e:
    				value = e
    	finally:
    		print("Don't forget to clean up when close() is called")
    
    >>>generator = echo(1)
    >>>print(next(generator))
    Execution starts when next() is called for the first time
    1
    >>>print(next(generator))
    None
    >>>generator.throw(TypeError, "spam")
    TypeError('spam',)
    >>>generator.close()
    Don't forget to clean up when close() is called
    ```
    

### Yield from

- Permette di delegare ad un generatore parti delle sue operazioni ad un altro generatore.
- yield from <expr> tratta l’espressione fornita come un subiterator. Tutti i valori prodotti dal subiterator sono passati direttamente al codice che ha invocato i metodi del generatore corrente.
- I valori passati da send() e qualsiasi eccezione passata da throw() sono passati all’iteratore sottostante se ha i metodi appropriati. Se non è questo il caso, send() lancia AttributeError o TypeError mentre throw() lancia l’eccezione passata come argomento a throw.

Per iteratori semplici, **yield from iterable** è equivalente a for item in iterable: yield item

```python
def g(x):
	yield from range(x, 0, -1)
	yield from range(x)

>>>list(g(5))
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
```

```python
def accumulate():
"""se viene inviato un valore con send(), somma il valore a tally. si interrompe se non è inviato nulla"""	
tally = 0
	while True:
		next = yield
		if next is None:
			return tally
		tally += next

def gather_tallies(tallies):
"""delega il lavoro ad accumulate per oSenere una somma che poi appende alla lista tallies"""
	while True:
		tally = yield from accumulate()
		tallies.append(tally)

tallies = []
acc = gather_tallies(tallies)
next(acc) #Assicura che acc sia pronto a ricevere valori (esecuzione si sospende allo yield)
for i in range(4)
	acc.send(i) #i valori vengono inviati ad acc e quindi ad accumulate
acc.send(None) # Fa terminare l’esecuzione di accumulate richiesta da gather tallies print(tallies)
print(tallies)
```

![Untitled](Untitled%202.png)

```python
def myGenerator(n):
	return myGeneratorAux(n,1,1)

def myGeneratorAux(n,c,p):
	if n==1: yield p
	else:
		yield p
		c=c+1
		p=c*p
		yield from myGeneratorAux(n-1,c,p)

if __name__=="__main__":
	print("I primi 6 faSoriali sono:")
	for x in myGenerator(6):
		print(x)

def inorderV(tree):
	if tree is not None:
		try:
			value, led, right = tree
		except ValueError: # wrong number to unpack
			print("Bad tree:", tree)
	else: # The following is one of 3 possible orders.
		yield from inorderV(led)
		yield value # Put this first or last for different orders.
		yield from inorderV(right)

tree = ('a', ('b', ('c',None,None), ('d', ('e', None, None), ('f', ('g', None, None), None))),
('h', None, ('i', ('l', ('m', None, None), None), None)))

print([x for x in inorderV(tree)])

>>>['c', 'b', 'e', 'd', 'g', 'f', 'a', 'h', 'm', 'l', 'i']
```