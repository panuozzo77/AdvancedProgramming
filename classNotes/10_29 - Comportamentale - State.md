# Comportamentale - State

È un design pattern comportamentale che consente ad un oggetto di modificare il proprio comportamento quando il suo stato interno cambia.

- Il comportamento di un oggetto dipende dal suo stato e deve cambiare comportamento durante l’esecuzione del programma in base al suo stato.
- Le operazioni contengono statement condizionali grandi che dipendono dallo stato dell’oggetto. Lo stato dell’oggetto è di solito rappresentato da una o più costanti numerate. Il pattern State inserisce ciascun caso dello statement condizionale in una classe separata.
    - ciò consente di trattare lo stato dell’oggetto come un vero e proprio oggetto che può cambiare indipendentemente da altri oggetti.
    
    ```python
    class State_d:
    	def __init__(self, imp):
    		self.__implementation = imp
    
    	def changeImp(self, newImp):
    		self.__implementation = newImp
    
    	def __getattr__(self, name):
    		return getattr(self.__implementation, name)
    
    class Implementation1:
    	def f(self):
    		print("fiddle de dum, fiddle de dee")
    
    	def g(self):
    		print("Eric the half a bee")
    
    	def h(self):
    		print("Ho ho ho, tee hee hee")
    	
    class Implementation2:
    	def f(self):
    		print("We're Knights of the Round Table.")
    
    	def g(self):
    		print("We dance whene'er we're able.")
    
    	def h(self):
    		print("We do routines and chorus scenes")
    
    def run(b):
    	b.f()
    	b.g()
    	b.h()
    	b.g()
    	
    b = State_d(Implementation1())  
    run(b) # esecuzione con Implementation 1
  
    b.changeImp(Implementation2())
    run(b) # cambiata Implementation 
    ```
    
## Esempio

- Immaginiamo di dover fornire una classe Multiplexer che ha due stati che influiscono sul comportamento dei metodi della classe.

- **attivo**: il multiplexer accetta connessioni, cioè coppie (nome evento, callback), dove ogni callback è un qualsiasi callable. Dopo che sono state stabilite le connessioni, ogni volta che viene inviato un evento al multiplexer, i callback associati all’evento vengono invocati. 

- **dormiente**: l’invocazione dei suoi metodi non ha effetto (safe mode)

In questo esempio creiamo delle funzioni callback che contano il numero di eventi che ricevono. Queste funzioni sono connesse ad un multiplexer attivo. Poi vengono inviati un numero di eventi random al multiplexer e stampati i conteggi tenuti dalle funzioni callback.

- Dopo aver inviato 100 eventi random, lo stato del multiplexer viene cambiato a dormiente e gli vengono inviati altri 100 eventi random, ciascuno di essi verrà ignoranto.
- Il multiplexer viene riportato nello stato attivo e gli vengono inviati altri 100 eventi random.
    
    ```python
    After 100 active events: cars=150 vans=42 trucks=14 total=206
    After 100 dormant events: cars=150 vans=42 trucks=14 total=206
    After 100 active events: cars=303 vans=83 trucks=30 total=416
    ```
    
1) Il main crea dei contatori. Le istanze sono create callable e possono essere usate come funzioni.
    
   - Le istanze di Counter mantengono dei contatori separati per ciascuno dei nomi passati come argomento, in assenza di nome, hanno un contatore singolo.
    
2) creiamo un multiplexer (già attivo) e vengono connesse le funzioni callback agli eventi.
    
3) abbiamo 3 eventi, cars, vans e trucks. Ognuna possiede una funzione connessa per il contatore che viene invocata ogni volta che vi è generato
    
```python
# questo è il main
totalCounter = Counter()
carCounter = Counter("cars")
commercialCounter = Counter("vans", "trucks")

multiplexer = Multiplexer()
for eventName, callback in (("cars", carCounter),
       ("vans", commercialCounter), ("trucks", commercialCounter)):
   multiplexer.connect(eventName, callback)
   multiplexer.connect(eventName, totalCounter)
```
    
4) sempre nel main, procediamo ad eseguire il codice inviando 100 eventi random al multiplexer
    
```python
for event in generate_random_events(100):
   multiplexer.send(event)
print("After 100 active events: cars={} vans={} trucks={} total={}".format(carCounter.cars, commercialCounter.vans,commercialCounter.trucks, totalCounter.count))
```
    
### Classe Counter
  
1) se nel costruttore non vengono passati nomi, crea un’istanza self.count e la usa come contatore anonimo.
  
2) altrimenti possiede dei contatori con gli stessi nomi presenti nella lista dei nomi.
  
3) ogni volta che viene invocata l’istanza di Counter, verifica chi è il chiamante. Se è anonimo incrementa il contatore anonimo, altrimenti recupera l’attributo corrispondente al nome dell’evento. Se non trova l’attributo la funzione getattr lancia AttributeError.
    
   ```python
   class Counter:
       def __init__(self, *names):
           self.anonymous = not bool(names)
           if self.anonymous:
               self.count = 0
           else:
               for name in names:
                   if not name.isidentifier():
                       raise ValueError("names must be valid identifiers")
                   setattr(self, name, 0)
    
       def __call__(self, event):
           if self.anonymous:
               self.count += event.count
           else:
               count = getattr(self, event.name)
               setattr(self, event.name, count + event.count)
   ```
    
La classe è molto semplice.
    
   ```python
   class Event:
       def __init__(self, name, count=1):
           if not name.isidentifier():
               raise ValueError("names must be valid identifiers")
           self.name = name
           self.count = count
   ```
    
- La classe Multiplexer ha 2 possibili stati. 

  - Con ACTIVE i metodi state-sensitive svolgono un lavoro utile.

  - Con DORMANT i metodi state-sensitive non fanno nulla.

- self.callbacksForEvent è un dizionario di coppie (nomeEvento, listaCallable)

- Il **metodo connect** è usato per creare un’associazione tra un evento con un certo nome e un callback. Se il nome dell’evento non è nel dizionario, il defaultdict garantisce che venga creato un elemento con chiave uguale al nome dell’evento e con valore uguale ad una lista vuota che verrà poi restituita.

- Se il nome dell’evento è già nel dizionario, restituisce la lista associata.

- In entrambi i casi, con append() viene aggiunta alla lista il callback da associare all’evento

- Il **metodo disconnect** se invocato senza specificare un callback, disconnette tutti i callback associati al nome dell’evento dato. Altrimenti rimuove solo il callback specificato dalla lista dei callback
    
   ```python
   class Multiplexer:
       ACTIVE, DORMANT = ("ACTIVE", "DORMANT")
    
       def __init__(self):
           self.callbacksForEvent = collections.defaultdict(list)
           self.state = Multiplexer.ACTIVE
    
       def connect(self, eventName, callback):
           if self.state == Multiplexer.ACTIVE:
               self.callbacksForEvent[eventName].append(callback)
    
       def disconnect(self, eventName, callback=None):
           if self.state == Multiplexer.ACTIVE:
               if callback is None:
                   del self.callbacksForEvent[eventName]
               else:
                   self.callbacksForEvent[eventName].remove(callback)
    
       def send(self, event):
           if self.state == Multiplexer.ACTIVE:
               for callback in self.callbacksForEvent.get(event.name, ()):
                   callback(event)
   ```
    
   - La classe Multiplexer ha gli stessi 2 stati di prima e lo stesso metodo __init__. Questa volta l’attributo state è una proprietà.
   - Questa versione di multiplexer non immagazzina lo stato come tale ma lo computa controllando se uno dei 2 metodi pubblici è stato settato ad un metodo privato attivo o passivo.
   - _active_connect è un metodo privato che può essere assegnato al corrispondente metodo pubblico self.connect se lo stato del multiplexer è ACTIVE. I metodi _active_disconnect e _active_send sono simili.
    
   ```python
   # sempre nel corpo della classe Multiplexer	
       @property
       def state(self):
           return (Multiplexer.ACTIVE if self.send == self.__active_send else Multiplexer.DORMANT)
    
       @state.setter
       def state(self, state):
           if state == Multiplexer.ACTIVE:
               self.connect = self._active_connect
               self.disconnect = self._active_disconnect
               self.send = self._active_send
    
           else:
               self.connect = lambda *args: None
               self.disconnect = lambda * args: None
               self.send = lambda *args : None
   ```

### Esercizio su State
[esercizio_svolto](/exercises/8_state/1_esercizio_proposto.py)
Immaginiamo che un bambino venga iscritto alla scuola media. Il bambino può essere in uno dei seguenti stati:
a. iscritto: il bimbo è inizialmente iscritto al primo anno
b. alSecondoAnno: il bimbo è promosso al secondo anno
c. alTerzoAnno: il bimbo è promosso al terzo anno
d. diplomato: al termine del terzo, il bimbo consegue il diploma di scuola media.
La classe Bambino ha il metodo succ() per passare allo stato successivo, il metodo pred() per passare a quello
precedente (retrocesso in caso di debiti formativi non recuperati) e il metodo salta_anno() per saltare un anno (da
iscritto si salta al terzo anno e dal secondo anno al diploma). Lo stato iscritto non ha stati che lo precedono; 
lo stato diplomato non ha stati che vengono dopo di esso.
La classe Bambino ha anche un metodo stampaStato() per stampare lo stato del bambino. 
Scrivere la classe Bambino usando un approccio state-specific in cui lo stato del bambino è una proprietà. Non usare altre classi
oltre la classe Bambino.