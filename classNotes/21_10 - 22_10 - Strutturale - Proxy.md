# Strutturale - Proxy

Questo pattern viene utilizzato per creare un oggetto che funge da intermediario o rappresentante di un altro oggetto per controllarne l'accesso. Il Proxy può essere utilizzato per vari scopi, come il controllo dell'accesso, la gestione della creazione ritardata di oggetti costosi, il monitoraggio o la registrazione delle richieste, e altro ancora.

In breve, il Proxy è una classe che funge da "procuratore" per un'altra classe, consentendo di aggiungere funzionalità aggiuntive o controlli senza dover modificare direttamente l'oggetto originale. Questo aspetto rende il Proxy un design pattern strutturale, in quanto si concentra sulla composizione degli oggetti e sulle relazioni tra di essi, anziché sulla creazione di nuovi oggetti o sui comportamenti di esecuzione.

- **Remote Proxy**: proxy per un oggetto in un diverso spazio di indirizzi (su server)
- **Virtual Proxy**: fornisce la lazy initialization per creare oggetti costosi su richiesta solo se necessari
- **Protection Proxy**: è usato quando vogliamo che il programmatore lato client non abbia pieno accesso all’oggetto
- **Smart Reference**: è usato per aggiungere azioni aggiuntive quando si accede ad un oggetto. Per esempio per mantenere traccia del numero di riferimenti ad un oggetto

```python
# esempio di proxy che non fa nulla in particolare se non utilizzare esattamente i metodi di Implementation
class Implementation:
    def f(self):
        print("Implementation.f()")
    
    def g(self):
        print("Implementation.g()")
    
    def h(self):
        print("Implementation.h()")

class Proxy:
    def __init__(self):
        self.__implementation = Implementation()

    # Passa le chiamate ai metodi all’implementazione:
    def f(self): self.__implementation.f() 
    def g(self): self.__implementation.g() 
    def h(self): self.__implementation.h()

    #altrimenti, se vogliamo fare una cosa fina:
    def __getattr__(self, name):
        return getattr(self.__implementation, name)

p = Proxy()
p.f(); p.g(); p.h()
```

### Esempio di Virtual Proxy

- Supponiamo di dover creare delle immagini “costruite a step”. Può risultare conveniente comporle solo alla fine.
- I moduli Image e cyImage creano le immagini in memoria.
- Voglia dei proxy leggeri che ci permettano di creare un’immagine solo quando sapremo di quale immagine avremo bisogno.
- L’interfaccia Image.Image si compone di 10 metodi + costruttori ed altri metodi di salvataggio e predefiniti per alcune figure.
<br><br>
- ImageProxy può essere usata al posto di Image.Image. Basta usare qualsiasi interfaccia che supporti Image.
- Un oggetto ImageProxy non salva un’immagine ma mantiene una lista di tuple di comandi dove il primo elemento di ciascuna tupla è una funzione od un metodo unbound ed i rimanenti elementi sono gli argomenti da passare quando la funzione o il metodo è invocato
- ImageProxy supporta pienamente i 4 metodi di Image.Image line(), rectangle(), ellipse() e set_pixel(). Ogni volta che ne viene invocato uno, questo è aggiunto in una lista di comandi.
- Solo quando si sceglie di salvare l’immagine, questa viene effettivamente creata e vengono eseguite tutte le funzioni nel buffer.

```python
class ImageProxy:

	def __init__(self, ImageClass, width=None, height=None, filename=None):
	    assert (width is not None and height is not None) or filename is not None
        self.Image = ImageClass
        self.commands = []
        if filename is not None:
            self.load(filename)
        else:
            self.commands = [(self.Image, width, height)]

	def load(self, filename):
        self.commands = [(self.Image, None, None, filename)]
     
	def set_pixel(self, x, y, color):
        self.commands.append((self.Image.set_pixel, x, y, color))
     
	def line(self, x0, y0, x1, y1, color):
        self.commands.append((self.Image.line, x0, y0, x1, y1, color))
     
	def rectangle(self, x0, y0, x1, y1, outline=None, fill=None):
        self.commands.append((self.Image.rectangle, x0, y0, x1, y1, outline, fill))
     
	def ellipse(self, x0, y0, x1, y1, outline=None, fill=None):
        self.commands.append((self.Image.ellipse, x0, y0, x1, y1, outline, fill))

	def save(self, filename=None):
		command = self.commands.pop[0] # salvo tutta la tupla dei comandi
		function, *args = command # inizio a scompattare, in function il nome del costruttore, tutto il resto va in args
		image = function(*args) # invoco function sugli argomenti
		for command in self.commands: # scandisco tutti i comandi (ho tolto col pop le rimanenti tuple)
			function, *args = command
			function(image, *args) # invoco function sugli argomenti
		image.save(filename) # uso il save di Image
		return image # restituisco l'immagine
```

- Se un metodo non supportato viene invocato (come pixel()) Python lancia AttributeError.
- Alternativamente, creiamo una vera immagine non appena uno di questi metodi è invocato, così userà la vera immagine per l’esecuzione.
- È utile compore l’immagine solo alla fine dell’esecuzione perché:
    - 1) non è detto che ci arrivi
    - 2) è sicuramente necessario lo sforzo richiesto alla macchina.
    

```python
class myClass:
    def __init__(self, x):
        self.value = x
        print('my variable is a ', type(self.value))

    def add10(self):
        self.value += 10

    def add_string(self):
        self.value += " Hello World!"

class myProxy:
    def __init__(self, value):
        self.__implementation = myClass(value)

    def __getattr__(self, name):
        return getattr(self.__implementation, name)

    def available_functions(self):
        implementation_attrs = dir(self.__implementation)
        method_names = [attr for attr in implementation_attrs if callable(getattr(self.__implementation, attr))]
        return method_names

    def print_value(self):
        print('the value is now: ', self.__implementation.value)

use = myProxy(5)
print(use.available_functions())
use.add10()
use.print_value()

>>my variable is a  <class 'int'>
>>['__class__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'add10', 'add_string']
>>the value is now:  15
```