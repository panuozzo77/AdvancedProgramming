# Creazionale - Prototype

- È usato per creare nuovi oggetti clonando un oggetto preesistente e poi modificando il clone così creato. 

  - Point è la classe preesistente:
      ```Python
      class Point:
    
          __slots__ = ("x", "y")
    
          def __init__(self, x, y):
              self.x = x
              self.y = y
      ```
  - In questo codice cloniamo nuovi punti in diversi modi: 
    ```Python
    def makeobject(Class, *args, **kwargs):
        return Class(*args. **kwargs)
    
    point1 = Point(1, 2)  #invochiamo il costruttore
    point2 = eval("{}({}, {})".format("Point", 2, 4))  #eval esegue il codice passato in argomento
    point3 = getattr(sys.modules[__name__], "Point")(3, 6) #getattr restituisce il valore dell'attributo nominato. sys.modules mappa i nomi dei moduli ai moduli caricati
    point4 = globals()["Point"](4, 8) #comportamento simile a getattr ma restituisce un dizionario che rappresenta la tavola dei simboli globali. Il dizionario è relativo al modulo dove è definita la funzione, non quello in cui è invocata
    point5 = make_object(Point, 5, 10)
    point6 = copy.deepcopy(point5) #clona un oggetto esistente poi lo inizializza con le istruzioni successive
    point6.x = 6
    point6.y = 12
    point7 = point1.__class__(7, 14) #__class__ contiene una classe a cui appartiene un'istanza
    ```
## Tutte le metodologie usate per copiare:
   - point1 = Point(1, 2)
     - È stato invocato il costruttore in modo statico. 
     - Vogliamo creare le istanze di Point in modo dinamico!
   - point2 = eval("{}({}, {})".format("Point", 2, 4))
     - eval() crea istanze di Point
     - perché valuta l'espressione Python rappresentata dalla stringa ricevuta come argomento. Esegue quindi il codice.
   - point3 = getattr(sys.modules[__name__], "Point")(3, 6)
     - getattr(object, name, default) restituisce il valore dell'attributo dell'oggetto
     - sys.modules è un dizionario che mappa i nomi dei moduli ai moduli che sono stati già stati caricati.
     - getattr(sys.modules[\_\_name__], "Point") restituisce il valore dell'attributo Point (la classe) dal modulo (il file eseguito)
   - point4 = globals()["Point"](4, 8)
     - globals() restituisce un dizionario che rappresenta la tavola dei simboli globali. All'interno di una funzione o un metodo, il dizionario è relativo al modulo dove è definita la funzione, non quello in cui è invocata.
     - molto simile a getattr()
   -  point5 = make_object(Point, 3,9)
     - usa la funzione make-object
   - point6 = copy.deepcopy(point5)
     - 1. clona un oggetto esistente
     - 2. lo inizializza con le istruzioni successive
   - point7 = point1.__class__(7, 14)
     - è creato usando point1
     - istanza.\_\_class__ contiene la classe a cui appartiene l'istanza.
### Note su eval()
- Gli argomenti sono una stringa e due argomenti opzionali __globals__ e __locals__
  - __globals__ deve essere un dizionario,
  - __locals__ può essere di un qualsiasi tipo mapping.
- La stringa passata come argomento viene valutata come un'espressone Python usando i dizionari globals e locals come namespace globali e locali.
- Se in __globals__ non è presente un valore per la chiave \_\_builtins__, un riferimento al modulo built-in è associato alla chiave \_\_builtins__ prima di fare il parsing dell'espressione.
- il valore di default di __locals__ è il dizionario __globals__
- Se entrambi i dizionari sono omessi, è eseguita con i __globals__ e __locals__ nell'ambiente in cui eval() è invocata.

```python
>>> x = 4
>>> y = 3
>>> s = eval("x + y")
>>> print(f"s: {s}")
s: 7

>>> t = eval('x + y', {'x’: 5, 'y': 8})
>>> print(f"t: {t}")
t: 13
```