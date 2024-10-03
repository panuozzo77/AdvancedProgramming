# Creazionale - Singleton

Il pattern Singleton è un pattern creazionale ed è usato quando abbiamo bisogno di una classe che ha un’unica istanza che è la sola ad essere usata dal programma. È utile nelle seguenti situazioni:

- Controllare l’accesso concorrente ad una risorsa condivisa.
- Se si ha bisogno di un punto globale di accesso per la risorsa da parti differenti del sistema.
- Quando si ha bisogno di un unico oggetto di una certa classe.

Implementazioni:

- Spooler di stampa.
- Gestione connessioni ai database.
- Trovare e memorizzare informazioni su un file di configurazione esterno.

```python
class Singleton:
	
		# storage for the instance reference
		__instance = None

		def __init__(self):
			""" Create singleton instance """
			# Check whether we already have an instance
			if Singleton.__instance is None:
				# Create and remember instance
				Singleton.__instance = Singleton.__impl()
			# Store instance reference as the only member in the handle
			self.__dict__['_Singleton__instance'] = Singleton.__instance

		def __getattr__(self, attr):
			""" Delegate access to implementation """
			return getattr(self.__instance, attr)

		def __setattr__(self, attr, value):
			""" Delegate access to implementation """
			return setattr(self.__instance, attr, value)
  
	#**statt accort** è una definizione di classe protetta dentro Singleton!
		class __impl:
			""" Implementation of the singleton interface """
		
			def spam(self):
				""" Test method, return singleton id """
				return id(self)
```

- se __init__ della nuova classe invoca __init__ di Singleton allora __init__ di Singleton non crea una nuova istanza (perché l’IF è False).
- se __init__ della nuova classe **non** invoca __init__ di Singleton, è evidente che non viene creata alcuna istanza perché la crea __init__ di Singleton.

```python
s1 = Singleton()
print(id(s1), s1.spam())

s2 = Singleton()
print(id(s2), s2.spam())

>> id(s1) è diverso da id(s2)
>> s1.spam() e s2.spam() invece è uguale
```

### FunFact su __getattr__ e __getattribute__

- Quando si accede ad un attributo di un’istanza di una classe viene invocato il metodo object.__getattribute__(self, name).
    - se __getattribute__ non è definito ma è implementato __getattr__ o l’esecuzione di __getattribute__lancia AttributeError allora esegue __getattr__().
- object.__getattr__(self, name) restituisce il valore dell’attributo o lancia l’eccezione AttributeError
- L’implementazione di __getattribute__() deve sempre invocare il metodo della classe base usando lo stesso nome per evitare la ricorsione infinita.

### Esempio di pattern Singleton: la classe Borg

- Nella classe Borg tutte le istanze sono diverse ma condividono lo stesso stato.
- Lo stato è condiviso dall’attributo shared_state e tutte le nuove istanze di Borg avranno lo stesso stato così come è definito dal metodo __new__
- In genere, lo stato di un’istanza è memorizzato nel dizionario __dict__ proprio dell’istanza. Nel codice in basso assegnamo la variabile di classe shared_state e tutte le istanze create

```python
class Borg():
	_shared_state = {}
	
	def __new__(cls, *args, **kwargs):
		obj = super().__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._shared_state
		return obj

#eseguiamo

class Child(borg):
	pass

>>borg = Borg()
>>another_borg = Borg()
>>borg is another_borg
False
>>child = Child()
>>borg.only_one_var = "I'm the only one var"
>>child.only_one_var
I'm the only one var
```

Se volessi definire una sottoclasse di Borg con un altro stato condiviso dobbiamo resettare _shared_state nella sottoclasse come segue

```python
class AnotherChild(Borg):
	_shared_state = {}

>>another_child = AnotherChild()
>>another_child.only_one_var
AttributeError: has no attribute 'shared_state'
```

### Secondo il Libro

Il modo più semplice per realizzare la funzionalità del singleton è di creare un modulo con lo stato globale di cui si ha bisogno mantenuto in variabili private. L’accesso è fornito esclusivamente da funzioni pubbliche.

Es: abbiamo bisogno di una funzione [ get() ]che restituisca un dizionario di quotazioni di valute dove ogni entry è del tipo (nomeChiave, tassoDiCambio).

La funzione potrebbe essere invocata più volte ma nella maggior parte dei casi i valori dei tassi verrebbero acquisiti una sola volta.

La funzione get() possiede un attributo rates che è il dizionario contenente i tassi di cambio delle valute. 

I tassi vengono prelevati da get() accedendo ad un file pubblicato sul web. Quindi o per raccoglierli o per aggiornarli.

### Module-Level Singleton

Tutti i moduli sono per loro natura dei singleton per il modo in cui vengono importati in Python:

1. Se il modulo è già stato importato, questo viene restituito. Altrimenti, dopo aver trovato il modulo, questo viene inizializzato e restituito.
2. Inizializzare il modulo significa eseguire un codice includendo tutti gli assegnamenti a livello del modulo.
3. Quando si importa un modulo per la prima volta, vengono fatte tutte le inizializzazioni. Quando si importa il modulo una seconda volta, Python non esegue l’inizializzazione.

```python
#singleton.py
only_one_var = "I'm only one var"
```

```python
# module1.py
import singleton
print(singleton.only_one_var)
singleton.only_one_var += "  after modification"
import module2
```

```python
#module2.py
import singleton
print (singleton.only_one_var)
```

```python
>>python module1.py
I'm only one var
I'm only one var after modification
```