# Strutturale - Decorator

- Serve quando vogliamo estendere le funzionalità di singoli oggetti dinamicamente.
- Ad esempio un sistema GUI dovrebbe consentire di aggiungere proprietà (come i bordi) o comportamenti (lo scrolling) ad ogni componente dell’interfaccia utente.
- Un modo per far questo è tramite l’ereditarietà. Ereditare un bordo da un’altra classe mette un bordo intorno ad ogni istanza della sottoclasse.
    - Ciò è poco flessibile perché la scelta di un bordo è fatta in modo statico. Non è possibile controllare come e quando decorare la componente con un bordo.
- Un altro approccio più flessibile consiste nel racchiudere la componente in un altro oggetto che si occupa di aggiungere il bordo.
- Questo oggetto è definito “decoratore”.
- Il decoratore inoltra richieste alla componente e può svolgere azioni aggiuntive, come aggiungere un bordo o altre proprietà.

### Il Pattern Decorator (è una funzione)

- Un decoratore *di funzione* è una funzione che ha come unico argomento una **funzione** e restituisce una funzione con lo stesso nome della funzione originale ma con ulteriori funzionalità.
- Un decoratore *di classe* è una funzione che ha come unico argomento una **classe** e restituisce una classe con lo stesso nome della classe originale ma con funzionalità aggiuntive.
    - I decoratori di classe possono a volte essere utilizzati come alternativa alla creazione di sottoclassi.
- In Python c’è un supporto built-in per i decoratori di funzioni e per i decoratori di classe

### Function Decorator

- Tutti i decoratori di funzione hanno la stessa struttura:
    - Creazione della funzione wrapper:
        - all’interno del wrapper invochiamo la funzione originale;
        - prima di invocare la funzione originale possiamo effettuare qualsiasi lavoro di pre-processing;
        - dopo la chiamata siamo liberi di acquisire il risultato, di fare qualsiasi lavoro di post-processing e di restituire qualsiasi valore vogliamo;
    - Alla fine restituiamo la funzione wrapper come risultato del decoratore e questa funzione sostituisce la funzione originale acquisendo il suo nome.
    - Si scrive il simbolo @, allo stesso livello di indentazione dello statement def, seguito immediatamente dal nome del decoratore.
        - è possibile applicare un decoratore ad una funzione decorata.
    
    ```python
    #la nostra funzione decoratore
    def float_args_and_return(function):
        def wrapper(*args, **kwargs):
            args = [float(arg) for arg in args]
            return float(function(*args, **kwargs))
        return wrapper
    
    @float_args_and_return
    def mean(first, second, *rest):
        numbers = (first, second) + rest
        return sum(numbers) / len(numbers)
    
    ```
    
    Con la versione decorata, mean(5, “6”, “7.5”) non genera alcun errore dal momento che viene effettuato il casting in numeri validi.
    
    È anche possibile creare una funzione senza decoratore ed aggiungerlo successivamente così:
    
    ```python
    def mean(first, second, *rest):
        numbers = (first, second) + rest
        return sum(numbers) / len(numbers)
    
    mean = float_args_and_return(mean)
    
    ```
    

### Analizziamo bene il codice di sopra

- La funzione *float_args_and_return()* è un decoratore di funzione per cui ha come argomento una singola funzione.
- Per convenzione, le funzioni wrapper hanno come argomenti un parametro che indica il numero variabile di parametri (*args) ed uno di tipo keyword (***kwargs)
- Eventuali vincoli sugli argomenti sono gestiti dalla funzione originale. Nel creare il decoratore, **dobbiamo solo assicurarci che alla funzione originale vengano passati tutti gli argomenti.**

### Problema di Documentazione del codice

- Una funzione decoratore avrà il valore dell’attributo __**name__** settato a **wrapper** invece che con il nome originale della funzione.
- Non ha docstring anche nel caso in cui la funzione originale abbia una docstring!
- Attraverso un ulteriore decoratore @functools.wraps per decorare la funzione wrapper possiamo assicurarci che gli attributi __name__ e __doc__ della funzione decorat contengano rispettivamente il nome e la docstring della funzione originale.
- È sempre consigliato usare il decoratore @functools.wrap dal momento che ci assicura che
    - nei traceback vengano visualizzati i nomi corretti delle funzioni
    - E si possa accedere alle docstring delle funzioni originali

```python
import functools

def float_args_and_return(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        args = [float(arg) for arg in args]
        return float(function(*args, **kwargs))
    return wrapper

```

Esercizio

- Scrivere il decoratore di funzione decf che fa in modo che venga lanciata l’eccezione TypeError se il numero di argomenti è diverso da due. Altrimenti, se la funzione decorata restituisce un risultato, questo viene aggiunto insieme al valore del primo argomento in un file di nome “risultato.txt”.
- Suggerimento: Ricordatevi di convertire a stringa il valore del primo argomento e il risultato quando li scrivete nel file e di aprire il file in modo da non cancellare quanto scritto precedentemente nel file.

```python
def decf(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if(len(args)+len(kwargs)=!2):
			raise TypeError("function must have 2 arguments!")
		else
			result = function(*args, **kwargs)
			#qui continuiamo a scrivere la funzione decoratore
			with open("risultato.txt", "a") as file:
				arg1 = str(args[0])
				result_str = str(result)
	
				file.write(arg1 + " + " result_str + " = " + str(float(arg1) + float(result_str)) + "\n")
			#abbiamo finito la funzione decoratore
		return result
	return wrapper

#ora utilizziamolo seriamente:

def somma(a, b)
	return a + b

try:
	somma(2, 3)
except TypeError as e:
	print(e)
```

- Scrivere il decoratore di funzione decora che trasforma la funzione decorata in una funzione che lancia l’eccezione TypeError se uno o più argomenti non sono di tipo str. La funzione deve restituire una stringa formata dagli argomenti ricevuti in input e dal risultato intervallati da uno spazio. Non dimenticate di convertire il risultato in stringa quando lo inserite nella stringa output.
- Esempio: se la funzione riceve in input “il” , “risultato”, “è”, la funzione non lancia l’eccezione e restituisce la stringa “Il risultato è …” dove al posto dei puntini deve apparire il risultato della funzione.

### Decoratori di Classe

- Sono molto simili ai decoratori di funzioni ma sono eseguiti al termine di uno statement class.
- I decoratori di classe sono funzioni che ricevono una classe come unico argomento e restituiscono una nuova classe con lo stesso nome della classe originale ma con funzionalità aggiuntive.
- Possono essere usati sia per gestire le classi dopo che esse sono state create sia per inserire un livello di logica extra (wrapper) per gestire le istanze della classe quando sono create

```python
def decorator(aClass): ...

@decorator
class C: ...
```

```python
def decorator(aClass): ...

class C: ...
C = decorator(C)
```

### Esempio di utilizzo

Può essere impiegato per dotare automaticamente le classi con una variabile numInstances per contare le istanze. Si può usare lo stesso approccio per aggiungere altri dati.

```python
def count(aClass):
    aClass.numInstances = 0
    return aClass

@count
class Spam:
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

class Sub(Spam):
    pass

class Other(Spam):
    pass

```

```python
OUTPUT
>>> from classdec0.py import Spam, Sub,
Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
3
>>> print(sub.numInstances)
3
>>> print(other.numInstances)
3

```

### Class Decorator e Costruttori

```python
def count(aClass):
	aClass.numInstances = 0
	return aClass

@count
class Spam:
	def __init__(self):
		Spam.numInstances =Spam.numInstances + 1

@count
	class Sub(Spam):
		pass

@count
class Other(Spam):
	def __init__(self):
		Other.numInstances =Other.numInstances + 1
```

```python
def count(aClass):
	aClass.numInstances = 0
	return aClass

@count
class Spam:
	@classmethod
	def count(cls):
		cls.numInstances+=1
	
	def __init__(self):
		self.count()

@count
class Sub(Spam):
	pass

@count
class Other(Spam):
	pass
```

Ogni classe ha una variabile numInstances. 

Quando viene creato un oggetto di tipo Sub è invocato __init__ della classe base Spam .

Quando viene creato un oggetto di tipo Other, viene invocato il **suo costruttore** ed è incrementato numInstances di Other

```python
>>> from classdec1.py import Spam, Sub, Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
2
>>> print(sub.numInstances)
0
>>> print(other.numInstances)
1
```

```python
>>> from classdec2.py import Spam, Sub, Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
1
>>> print(sub.numInstances)
1
>>> print(other.numInstances)
1
>>> other=Other()
>>> print(other.numInstances)
2
>>> print(spam.numInstances)
1
>>> print(sub.numInstances)
1
```

Qui invece abbiamo ridefinito il costruttore, utilizzandone ben 2 in una sola chiamata, osserviamo bene:

```python
def count(aClass):
	aClass.numInstances = 0
	**oldInit=aClass.__init__**
	
	def __newInit__(self,*args,**kwargs):
		aClass.numInstances+=1
		**oldInit(self,*args,**kwargs)**

#questo è il vecchio init
	aClass.__init__=__newInit__
		return aClass

@count
class Spam:
	pass

@count
class Sub(Spam):
	pass

@count
class Other(Spam):
	pass
```

```python
>>> from classdec3.py import Spam, Sub, Other
>>> spam=Spam()
>>> sub=Sub()
>>> other=Other()
>>> print(spam.numInstances)
3
>>> print(sub.numInstances)
1
>>> print(other.numInstances)
1
>>> other=Other()
>>> print(other.numInstances)
2
>>> print(spam.numInstances)
4
>>> print(sub.numInstances)
1
```

Possiamo vedere che ogni classe possiede una propria variabile numInstances ma, ad ogni chiamata del costruttore viene incrementata sia quella delle sottoclassi che quella della classe genitore.

---

### Considerazioni sul ridefinire il costruttore

count pone oldinit=aClass.__init__ e poi definisce la funzione __newInit__ in modo che invochi oldInit e non aClass.__init__. 
Se __newInit__ avesse invocato aClass.__init__ allora, nel momento in cui avessimo creato un’istanza di una delle classi decorate con count, il metodo __init__ della classe (rimpiazzato da __newInit__) avrebbe lanciato l’eccezione RecursionError.

Questa eccezione indica che è stato ecceduto il limite al numero massimo di chiamate ricorsive possibili. 

Questo limite evita un overflow dello stack e un conseguente crash di Python. 

L’eccezione sarebbe stata causata da una ricorsione infinita innescata dall’invocazione di aClass.__init__ di __newInit__.

A causa del **late binding**, il valore di aClass.__init__ nella chiusura di __newInit__ è stabilito quando __newInit__ è eseguita. Siccome quando __newInit__ si ha che aClass.__init__ è stato sostituito dal metodo __newInit__ allora __newInit__ avrebbe invocato ricorsivamente se stesso.

### Late Binding

In Python i valori delle variabili usati nelle funzioni vengono osservati al momento della chiamata alla funzione. 
In questo esempio, quando vengono invocate le funzioni inserite in listOfFunctions, il valore di m è 3 perché il for è già terminato e il valore di m al termine del ciclo è 3.

Ciascuna funzione aggiunta alla lista computa m*n ed m assume come ultimo valore 3. Di conseguenza, la funzione calcola sempre 3*n.

```python
listOfFunctions=[]
for m in [1, 2, 3]:
	def f(n):
		return m*n
	listOfFunctions.append(f)

for function in listOfFunctions:
	print(function (4))
```

```python
Inaspettatamente il for alle linee 6 e 7 stampa
12
12
12
e non
4
8
12
```

## Chiusura

Nella programmazione funzionale il termine chiusura indica la capacità di una funzione di ricordare valori presenti negli scope in cui essa è racchiusa a prescindere dal fatto che lo scope sia presente o meno in memoria quando la funzione è invocata. 

Scope delle funzioni innestate:

- Una funzione innestata è definita all’interno di un’altra funzione
- Una funzione innestata può accedere allo scope della funzione che la racchiude, detto non-local scope
    - Per default queste variabili sono di sola lettura e per modificarle occorre dichiararle non-local con la keyword nonlocal
- Una funzione inner definita all’interno di una funzione outer “ricorda” un valore dello scope di outer anche quando la variabile scompare dallo scope o la funzione outer viene rimossa dal namespace.

```python
x = 24
y = 33
def outer():
	z = 100
	def inner():
		nonlocal z
		print("il valore di z stampato da inner è:", z)
		z=5

			def innerinner():
				print("il valore di z stampato da innerinner è ", z)
			return innerinner
	return inner

f=outer() //f e` la funzione inner restituita da outer
g=f() //g e` la funzione innerinner restituita da f
g() //stampa “il valore…”
```

### Attributi Proprietà

La funzione built-in property permette di associare operazioni di fetch e set ad attributi specifici.

property(fget=None, fset=None, fdel=None, doc=None) restituisce un attributo property

- fget è una funzione per ottenere il valore di un attributo
- fset è una funzione per settare un attributo
- fdel è una funzione per cancellare un attributo
- doc crea una docstring dell’attributo

Se c è un’istanza di C, c.x = value invoca il setter *setx* e del c.x invocherà *del x.*

Se fornita, doc sarà la docstring dell’attributo property. In caso contrario, viene copiata la docstring di fget (se c’è)

```python
class C:
	def __init__(self):
		self._x = None
	def getx(self): return self._x
	def setx(self, value): self._x = value
	def delx(self): del self._x

	x = property(getx, setx, delx, "I'm the 'x' property")
```

```python
#se usiamo il decoratore @property possiamo trasformare un metodo in un "getter". per l'attributo read-only voltage e settare la docstring di voltage a "get the current voltage"

class Parrot:
	def __init__(self):
		self._voltage(100000)

	@property
	def voltage(self)
		"""Get the current Voltage"""
		return self._voltage
```

possiamo implementare anche i metodi getter, setter e deleter attraverso altri decoratori per creare una copia della proprietà con la corrispondente funzione accessoria uguale alla funzione decorata. [Codici Equivalenti]

```python
class C:
	def __init__(self):
		self._x = None
	
	@property
	def x(self)
		"""I'm the x property"""
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@x.deleter
	def x(self)
		del self._x
```

```python
class C:
	def __init__(self):
		self._x = None
	
	def getx(self): return self._x

	def setx(self, value): self._x = value

	def delx(self): del self._x
		
	x = property(getx, setx, delx, "I'm the 'x' property.")
```

---

### Class Decorator e Proprietà

È abbastanza comune creare classi che hanno molte proprietà read-write. Tali classi hanno molto codice duplicato o parzialmente duplicato per i getter e setter.

Es: una classe Book ha il titolo, ISBN, prezzo, quantità. Vorremmo avere 4 decoratori @property con codice pressoché uguale. 

I decoratori di classe consentono di evitare la duplicazione del codice. 

```python
@ensure("title", is_non_empty_str)
@ensure("isbn", is_valid_isbn)
@ensure("price", is_in_range(1, 10000))
@ensure("quantity", is_in_range(0, 1000000))
class Book:
	def __init__(self, title, isbn, price, quantity):
	 self.title = title
	 self.isbn = isbn
	 self.price = price
	 self.quantity = quantity

	@property #questo è un getter
	def value(self):
		return self.price * self.quantity
```

Nel codice applico 4 volte @ensure per creare le 4 proprietà in questo ordine: quantity, price, isbn, title.

self.title, self.isbn, self.price, self.quantity sono proprietà per cui gli assegnamenti che avvengono in **init**() sono tutti effettuati dai setter delle proprietà

- Una breve nota sul funzionamento di property
    
    Scenario del mondo reale:
    
    Abbiamo una classe House che possiede un suo prezzo. Così:
    
    ```python
    class House:
    
    	def __init__(self, price):
    		self.price = price
    ```
    
    L’attributo è pubblico. Possiamo fare: 
    
    ```python
    h = House(10)
    print(h.price)
    
    h.price = -10
    
    ```
    
    Ma questo non va bene! Magari non vogliamo che abbia valori negativi. Vogliamo avere alcune validazioni sul codice prima che questo venga assegnato. La prima cosa che ci viene in mente è quello di definire dei metodi ad-hoc come get_price o set_price che facciano quello che vogliamo. Possiamo invece evitare tutto questo attraverso il decoratore @property. Senza nulla accanto definisce un metodo getter, altrimenti con .setter o .deleter utilizza il codice che scriveremo noi. E noi potremo comunque utilizzare il metodo di accesso “semplice” con h.price per ottenerlo o h.price = 123 per settarlo.
    
    In questo modo, nel caso avessimo già scritto tutto il codice per il nostro progetto, non dovremmo stravolgerlo interamente. 
    
    ```python
    class House:
    
    	def __init__(self, price):
    		self._price = price
    
    	@property
    	def price(self):
    		return self._price
    	
    	@price.setter
    	def price(self, new_price):
    		if new_price > 0 and isinstance(new_price, float):
    			self._price = new_price
    		else:
    			print("Please enter a valid price")
    
    	@price.deleter
    	def price(self):
    		del self._price
    ```
    

Una modifica per applicare un unico decoratore di classe

```python
@do_ensure
class Book:
	title = Ensure(is_non_empty_str)
	isbn = Ensure(is_valid_isbn)
	price = Ensure(is_in_range(1, 10000))
	quantity = Ensure(is_in_range(0, 1000000))

	def __init__(self, title, isbn, price, quantity):
		self.title = title
		self.isbn = isbn
		self.price = price
		self.quantity = quantity

	@property
	def value(self):
		return self.price * self.quantity
```

```python
class Ensure:
	def __init__(self, validate, doc=None):
		self.validate = validate
		self.doc = doc
```

- Utilizzare molti decoratori non è consigliato.
- Creiamo le 4 proprietà attraverso il costruttore della classe Ensure
- Il costruttore associa le proprietà all’istanza di book creata
- Lo scopo del decoratore di classe è rimpiazzare le 4 istanze di Ensure con una proprietà con lo stesso nome della corrispondente istanza di Ensure. Ciascuna proprietà utilizzerà la funzione di validazione passata al suo interno.

```python
def do_ensure(Class):
	def make_property(name, attribute): # questo è il nostro wrapper
		privateName = "__" + name   # si occupa di creare un attributo e poi di associarci la proprietà
	
		def getter(self): # restituisce il valore dell'attributo
			return getattr(self, privateName) 
	
		def setter(self, value): # il setter controlla prima della definizione se soddisfi la proprietà
			attribute.validate(name, value)
			setattr(self, privateName, value)

		return property(getter, setter, doc=attribute.doc)
	#questi 3 metodi di sopra vengono invocati solo dal for di sotto
	
	for name, attribute in Class.__dict__.items(): # cerca in questa classe quali sono gli attributi di tipo Ensure
		if isinstance(attribute, Ensure): # se soddisfa la proprietà
			setattr(Class, name, make_property(name, attribute)) # creo la proprietà
	return Class #restituisce la classe modificata
```

- avremmo potuto evitare la funzione innestata e porre il codice di quella funzione dopo il test isinstance().
- Ciò però non funziona a causa del late-binding
- Per risolvere è sufficiente usare una funzione separata (possibilmente innestata)

### Class Decorator vs Derivazioni di Classi

Può risultare conveniente ereditare i metodi nelle sottoclassi.

Se però questi non vengono mai modificati nelle sottoclassi, è possibile utilizzare un decoratore di classe per ottenere lo stesso risultato.

**Classe Base**

```python
class Mediated:
	
	def __init__(self):
		self.mediator = None

	def on_change(self):
		if self.mediator is not None:
			self.mediator.on_change(self)
```

Invocazione

```python
class hier(Mediated):
	pass

#eseguo
c = hier()
c.super().on_change()
```

**Decoratore di Classe**

```python
def mediated(Class):
	setattr(Class, "mediator", None)
	
	def on_change(self):
		if self.mediator is not None:
			self.mediator.on_change(self)
	setattr(Class, "on_change", on_change)
return Class
```

Invocazione

```python
@mediated
class hier:
	pass
#eseguo
c = hier()
c.on_change()
```