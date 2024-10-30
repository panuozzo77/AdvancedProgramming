## Decoratori di Classe

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
>>> from classdec0.py import Spam, Sub
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

## Class Decorator e Costruttori

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
>>> spam = Spam()
>>> sub = Sub()
>>> other = Other()
>>> print(spam.numInstances)
2
>>> print(sub.numInstances)
0
>>> print(other.numInstances)
1
```

Ogni classe ha una variabile numInstances. 

Quando viene creato un oggetto di tipo Sub è invocato __init__ della classe base Spam, in quanto non presente il costruttore per Sub ed è incrementato numInstances di Spam.

Quando viene creato un oggetto di tipo Other, viene invocato il **suo costruttore** che è stato definito ed è incrementato numInstances di Other, senza risalire la gerarchia

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
## Ridefinire costruttori, esempio **\_\_newInit__**
Qui invece abbiamo ridefinito il costruttore, utilizzandone ben 2 in una sola chiamata, osserviamo bene:

```python
def count(aClass):
	aClass.numInstances = 0
	**oldInit=aClass.__init__**
	
	def __newInit__(self,*args,**kwargs):
		aClass.numInstances+=1
		**oldInit(self,*args,**kwargs)** # lo invoco per ottenere quello che avrei con l'init di partenza, non si sa magari perdo qualche variabile...

#questo è il vecchio init
	aClass.__init__=__newInit__ ## faccio eseguire il nuovo init
		return aClass ## restituisco così la classe modificata

@count
class Spam:
	pass

@count
class Sub(Spam):
	pass

@count
class Other(Spam):
	pass

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

Possiamo vedere che ogni classe possiede una propria variabile numInstances ma, ad ogni chiamata del costruttore viene incrementata sia quella delle sottoclassi che quella della classe genitore. Questo perché:
- Spam era senza init (aveva ereditato l'init di Object), gliene provvediamo uno attraverso il decoratore
- Sub ed Other ereditano l'init di Spam, quindi ad ogni chiamata iniziano anche l'init di Spam, ma ciascuna classe possiede anche una sua variabile di classe per contare le istanze, quindi incrementano in maniera duplice il contatore

---

### Considerazioni sul ridefinire il costruttore

count pone oldinit=aClass.__init__ e poi definisce la funzione __newInit__ in modo che invochi oldInit e non aClass.__init__. 
Se __newInit__ avesse invocato aClass.__init__ allora, nel momento in cui avessimo creato un’istanza di una delle classi decorate con count, il metodo __init__ della classe (rimpiazzato da __newInit__) avrebbe lanciato l’eccezione RecursionError.

Questa eccezione indica che è stato ecceduto il limite al numero massimo di chiamate ricorsive possibili. 

Questo limite evita un overflow dello stack e un conseguente crash di Python. 

L’eccezione sarebbe stata causata da una ricorsione infinita innescata dall’invocazione di aClass.__init__ di __newInit__.

A causa del **late binding**, il valore di aClass.__init__ nella chiusura di __newInit__ è stabilito quando __newInit__ è eseguita. Siccome quando __newInit__ si ha che aClass.__init__ è stato sostituito dal metodo __newInit__ allora __newInit__ avrebbe invocato ricorsivamente se stesso.