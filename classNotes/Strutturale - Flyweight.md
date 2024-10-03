# Strutturale - Flyweight

È concepito per gestire un grande numero di oggetti relativamente piccoli dove molti sono duplicati l’uno dell’altro. 

- Il pattern è implementato in modo da avere un’unica istanza per rappresentare tutti gli oggetti uguali tra loro. Ogni volta che è necessario, questa unica istanza viene condivisa.
- Python permette di implementare Flyweight in modo naturale grazie all’uso dei riferimenti
- Il modo più semplice per trarre vantagio è usare un dict, in cui ciascun oggetto (unico) corrisponde ad un valore identificato da un’unica chiave.
    - Ciò assicura che ciascun oggetto distinto venga creato un’unica volta
- In alcune situazioni si potrebbero avere molti oggetti non piccoli dove gran parte di essi o tutti sono unici. Un facile modo per ridurre l’uso dela memoria è usare __slots__

__Slots__

- Ogni classe può avere attributi di istanza.
- Python di default salva gli attributi in un dict. È utile perché ci permette di settare attributi durante l’esecuzione.
- Comunque classi piccole con attributi noti potrebbero portare a colli di bottiglia perché il dict è uno spreco di RAM.
- Attraverso __slots__ indichiamo a Python di non usare un dict e di allocare lo spazio sufficiente per un insieme fissato di attributi.

```java
class MyClass():
	def __init__(self, name, identifier):
		self.name = name
		self.identifier = identifier

class MyClass():
	__slots__ = [‘name’, 'identifier’]
	def __init__(self, name, identifier):
		self.name = name
		self.identifier=identifier
```

```java
class Point:

	__slots__ = ("x", "y", "z", "color")

	def init__(self, x=0, y=0, z=0, color=None):
	 self.x = x
	 self.y = y
	 self.z = z
	 self.color = color
```

Un programma per creare una tupla di un milione di punti ha impiegato su una stessa macchina
• nella versione con slots, circa 2 secondi e il programma ha occupato 183 Mebibyte di RAM
• nella versione senza slots, una frazione di secondo in meno ma il programma ha occupato 312 Mebibyte di RAM

Consumare memoria consente di avere maggiore velocità. Ma questo dipende dalle priorità.

```java
class Point:
	 __slots__ = ()
	 __dbm = shelve.open(os.path.join(tempfile.gettempdir(), "point.db"))

	def init__(self, x=0, y=0, z=0, color=None): #questo metodo assegna i valori delle variabili in un file DBM
	 self.x = x
	 self.y = y
	 self.z = z
	 self.color = color

	def __getattr__(self, name):
		return Point.__dbm[self.__key(name)] #questo metodo è invocato ogni volta che si accede ad un attributo della classe

	def __setattr__(self, name, value): #ogni volta che si setta un attributo si chiama questo metodo
	 Point.__dbm[self.__key(name)] = value #il valore è immagazzinato dopo essere stato convertito in un flusso di byte

	def __key(self, name):
		return "{:X}:{}".format(id(self), name) #fornisce una stringa chiave per ognuno degli attributi. La chiave è ottenuta
																						#dall'ID restituita da id(self) in esadecimale e dal nome dell'attributo
```

Questa nuova classe utilizza un database DBM (chiave-valore) immagazzinato in un file su disco.

Un riferimento al DBM è mantenuto nella variabile Point.__dbm.

Tutti i punti condividono lo stesso file DBM.

shelve.open apre un dizionario persistente.

Il filename specificato è il nome di base per il database sottostante.

Per default il file database è aperto in lettura e scrittura. Se non esiste viene creato.

Il modulo shelve serializza i valori immagazzinati e li deserializza quando vengono recuperati dal database.

Il processo di deserializzazione in Python non è sicuro perché esegue codice arbitrario e non può mai essere effettuato su dati provenienti da fonti non affidabili. 

Le chiavi e valori dei database DBM devono essere in byte. Python accetta sia stringhe che byte e le converte in stringhe di byte. Un valore recuperato dal database è convertito dalla rappresentazione sotto forma di sequenza di bytes nel tipo originario. 

Sulla macchina usata per i test, la creazione di un milione di punti ha richiesto circa un minuto ma il programma ha occupato solo 29 Mebibyte di RAM, mentre la versione precedente 183 Mebibyte