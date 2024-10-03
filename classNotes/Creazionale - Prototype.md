# Creazionale - Prototype

È usato per creare nuovi oggetti clonando un oggetto preesistente e poi modificando il clone così creato. 

```java
class Point:

	__slots__ = ("x", "y")

	def __init__(self, x, y):
		self.x = x
		self.y = y
```

```java
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