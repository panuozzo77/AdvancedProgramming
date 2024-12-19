# Il modulo Inspect
- Il modulo inspect fornisce diverse utili funzioni per aiutare a ottenere informazioni riguardanti oggetti "vivi" come moduli, classi, metodi, funzioni, traceback, oggetti frame e oggetti codice.
- Per esempio, può essere d'aiuto per esaminare i contenuti di una classe, accedere al codice sorgente di un metodo, estrarre e formattare la lista di argomenti di una funzione, o ottenere tutte le informazioni necessarie per mostrare un traceback dettagliato.
- Ci sono quattro principali tipi di servizi forniti da questo modulo: effettuare il type checking, prelevare il codice sorgente, ispezionare classi e funzioni, esaminare lo stack dell'interprete.

## metodo inspect.getmembers
- inspect.getmembers(object [,predicate])
  - restituisce tutti i membri di un oggetto in una lista di coppie (name, values)
  - se viene fornito anche l'argomento opzionale __predicate__ questo viene invocato con l'oggetto value di ciascuna coppia e vengono incluse nella lista solo le coppie per le quali il predicato restituisce un valore true

| **Funzione**     | **Descrizione**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| `ismodule()`      | Return true if the object is a module.                                                            |
| `isclass()`       | Return true if the object is a class, whether built-in or created in Python code.                 |
| `ismethod()`      | Return true if the object is a bound method written in Python.                                    |
| `isfunction()`    | Return true if the object is a Python function, which includes functions created by a lambda expression. |
| `isgenerator()`   | Return true if the object is a generator.                                                         |
| `iscode()`        | Return true if the object is a code.                                                              |
| `isbuiltin()`     | Return true if the object is a built-in function or a bound built-in method.                      |
| `isabstract()`    | Return true if the object is an abstract base class.                                              |

```python
# modulo.py

'''Docstring del modulo'’’
import inspect
    def funzione():
        '''Docstring di funzione'''
        print ('Sono funzione')

class Base:
    '''Docstring di Base'''
    def __init__(self):
        self.var='Sono funzione'

    def funzione(self):
        print (self.var)

class Derivata(Base):
    def funzione(self):
        super().funzione()
        print ("Sono funzione di Derivata")
```

```python
import modulo
import inspect
import sys
for k,v in inspect.getmembers(sys.modules["modulo"], inspect.isclass):
print (k,v)

>>> Base <class 'moduloinspect.Base'>
>>> Derivata <class 'moduloinspect.Derivata'>
```

## metodo inspect.getmodulename
- Restituisce il nome del modulo (senza l’estensione) indicato da path (stringa che specifica l’intero path per arrivare al modulo) senza includere i nomi dei pacchetti. Viene controllata l’estensione con tutte le entrate di importlib.machinery.all_suffixed(). Se l’estensione corrisponde a una presente nella lista restituita da importlib.machinery.all_suffixed() (tale lista contiene le estensioni dei file importabili con import) allora viene restituita la componente finale della path senza l’estensione altrimenti viene restituito None.

## metodo inspect.getdoc
- Restituisce la stringa di documentazione per un oggetto ripulita degli spazi di indentazione da cleandoc().
- Se per l’oggetto non è fornita una stringa di documentazione e l’oggetto è una classe, un metodo, una property o un descrittore allora la stringa di documentazione è ottenuta dalla gerarchia.
- Restituisce None se la documentazione è assente o se è errata

## metodo inspect.getcomments
- Restituisce in una singola stringa le linee di commento che precedono il codice sorgente dell’oggetto (per una classe, metodo o funzione) o quelli in alto nel file sorgente (se l’oggetto è un modulo)
- Se il codice sorgente non è disponibile (ad esempio se l’oggetto è definito in C o da shell) allora viene restituito None.

```python
#script da eseguire, usando le classi Base e Derivata poc'anzi definite
import modulo
import inspect
import sys
print(inspect.getdoc(modulo))
print(inspect.getdoc(modulo.Base))
print(inspect.getdoc(modulo.funzione))
print(inspect.getcomments(sys.modules[__name__]))

>>> Docstring del modulo
>>> Docstring di Base
>>> Docstring di funzione
>>> #script da eseguire
```

## metodo inspect.getfullargs
- Restituisce i nomi e i valori di default dei parametri di una funzione Python. Restituisce una nametuple
- FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)
- __args__ è una lista dei nomi dei parametri posizionali
- varargs è il nome del parametro * o None in assenza del parametro preceduto da *
- kwonlyargs è una lista di parametri keyword-only nell’ordine in cui sono dichiarati.
- varkw è il nome del parametro ** o None in assenza del parametro preceduto da **
- defaults è una n-upla di argomenti di default corrispondentti agli ultimi n argomenti
posizionali
- kwonlydefaults è un dizionario che mappa i nomi dei parametri da kwonlyargs ai valori di default usati se nessun argomento viene fornito.
- annotations è un dizionario che mappa i nomi dei parametri alle annotazioni. La chiave speciale "return" è usata per l’annotazione del valore di return.

```python
# esempio di getfullargs
def strictly_typed(function):
    # Recupera le annotazioni dei tipi dai metadati della funzione
    annotations = function.__annotations__

    # Ottiene la specifica degli argomenti della funzione, inclusi argomenti posizionali e keyword-only
    arg_spec = inspect.getfullargspec(function)

    # Controlla che ci sia un'annotazione per il valore di ritorno
    assert "return" in annotations, "missing type for return value"

    # Controlla che ogni argomento abbia un'annotazione
    for arg in arg_spec.args + arg_spec.kwonlyargs:
        assert arg in annotations, f"missing type for parameter '{arg}'"

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        # La funzione wrapper comincia iterando su ogni coppia nome-argomento.
        # Siccome zip restituisce un iteratore e dictionary.items() restituisce una view,
        # non li possiamo concatenare direttamente. Per questo motivo li convertiamo in liste.
        for name, arg in (list(zip(arg_spec.args, args)) + list(kwargs.items())):
            # Controlla che il tipo di ogni argomento corrisponda a quello specificato
            assert isinstance(arg, annotations[name]), (
                f"expected argument '{name}' of {annotations[name]} got {type(arg)}"
            )
        
        # Invoca la funzione originale
        result = function(*args, **kwargs)

        # Controlla che il tipo del valore di ritorno corrisponda a quello specificato
        assert isinstance(result, annotations["return"]), (
            f"expected return of {annotations['return']} got {type(result)}"
        )

        # Restituisce il valore della funzione originale
        return result

    return wrapper

```

```python
@strictly_typed
def range_of_floats(a:int,b:int,c:int) -> types.GeneratorType:
    return (float(x) for x in range(a,b,c))

for x in range_of_floats(1,8,'a'):
    print(x)
```
```python
Traceback (most recent call last):
  File "/Users/adb/Documents/strictly_typed_decorator.py", line 31, in <module>
    for x in range_of_floats(1,8,'a'):
  File "/Users/adb/Documents/strictly_typed_decorator.py", line 16, in wrapper
    assert isinstance(arg, annotations[name]), (
AssertionError: expected argument 'c' of <class 'int'> got <class 'str'>
```

### altri metodi
- inspect.getfile(object) restituisce il nome del file in cui un oggetto è stato definito. Lancia TypeError se l'oggetto è un modulo, una classe o una funzione built-in.
- inspect.getmodule(object): prova ad indovinare in quale modulo un oggetto è stato definito. Restituisce None se non riesce ad individuare il modulo.
- inspect.getsourcefile(object): restituisce il nome del file sorgente Python nel quale un oggetto è stato definito oppure None se non c'è modo di individuare la sorgente. Lancia TypeError se l'oggetto è un modulo, una classe o una funzione built-in.
- inspect.getsource(object): restituisce in una singola stringa il testo del codice sorgente di un oggetto. L'argomento può essere un modulo, una classe, un metodo, una funzione, un traceback, un frame, o un oggetto code. Viene lanciato OSError se il codice sorgente non può essere recuperato.

## metodo inspect.signature
inspect.signature(callable, *, follow_wrapped=True, globals=None, locals=None, eval_str=False)
- Restituisce un oggetto Signature per callable
- Gli argomenti follow_wrapped, globals, locals, eval_str sono passati a inspect.get_signature per risolvere le annotazioni nel caso in cui si utilizzi from \_\_future__import annotations
- L'oggetto Signature rappresenta una chiamata di un callable e la sua annotazione per il return.
```python
from inspect import signature
def foo(a, *, b:int, **kwargs):
    pass

sig = signature(foo)

str(sig)
>>> '(a, *, b:int, **kwargs)'

str(sig.parameters['b'])
>>> b:int

str(sig.parameters['b']).annotation
>>> <class 'int'>

``` 

## classe inspect.Signature
- Per ogni parametro accettato dalla funzione l’oggetto Signature memorizza un oggetto Parameter nella sua collezioni di parametri parameters che è un mapping ordinato di coppie (nome parametro, oggetto Parameter). L’ordine è quello in cui sono definiti.
- Per settare parameters viene utilizzato l’argomento opzionale parameters che è una sequenza di oggetti parameter che viene validata verificando che non vi siano nomi di parametri duplicati, che i parametri siano nell’ordine corretto, cioe` prima quelli solo posizionali e poi quelli che possono essere considerati posizionali o keyword, e che i parametri con valori di default seguano quelli senza valori di default.
- L’argomento return_annotation è l’annotazione per il valore di return. Se il callable non ha l’annotazione per il return allora l’argomento e quindi l’attributo return_annotation della signature è settato a Signature.empty.

## metodi mind e bind_partial di Signature
- bind(*args, **kwargs)
  - Crea un mapping dagli argomenti posizionali o keyword ai parametri
  - Se *args e **kwargs corrispondono ai parametri nella signature su cui è invocato, bind restituisce un'istanza di inspect. BoundArguments che mantiene l'associazione tra parametri e argomenti. In caso contrario lancia TypeError.
- bind_partial(*args, **kwargs)
  - Funziona allo stesso modo di Signature.bind() ma permette di omettere alcuni argomenti.
  - Se *args e **kwargs corrispondono alla signature su cui è invocato, bind restituisce un'istanza di inspect.BoundArguments che mantiene l'associazione tra parametri. In caso contrario lancia TypeError

```python
import inspect

def bind_arguments(func,*args) -> inspect.BoundArguments:
    """ Controlla se gli argomenti args dati rispettano la
    signature"""
    try:
        return inspect.signature(func).bind(*args)
    except TypeError as e:
        print("argomenti non corrispondenti alla signature")

def f(x):
    return x+4

print(bind_arguments(f,3))
print(bind_arguments(f,4,3))

>>> <BoundArguments (x=3)>
>>> argomenti non corrispondenti alla signature 
    None
```

```python
import inspect

def bind_partial_arguments(func,*args) -> inspect.BoundArguments:
    """ Controlla se gli argomenti args dati rispettano la
    signature"""
    try:
        return inspect.signature(func).bind_partial(*args)
    except TypeError as e:
        print("argomenti non corrispondenti alla signature")

def f(x, y):
    return x+y

print(bind_arguments(f,3))
print(bind_arguments(f,4,3))

>>> <BoundArguments (x=3)>
>>> <BoundArguments (x=4, y=3)>
```

## metodo Signature.replace
- Gli oggetti Signature sono immutable, replace di inspect.Signature serve per creare una copia modificata di un oggetto Signature.
- replace(*[, parameters], [, return_annotation])
  - crea una nuova istanza di Signature basata sull'istanza di Signature su cui replace è invocata.
  - È possibile passare parametri e/o return_annotation differenti per sovrascrivere quelli della signature di partenza. Per rimuovere return_annotation dalla signature occorre passare Signature.empty
```python
def test(a, b):
    pass

sig = signature(test)

new_sig = sig.replace(return_annotation="new return anno")
str(new_sig)

>>> "(a, b) -> "new return anno""
```

## classe inspect.Parameter
class inspect.Parameter(name, kind, *, default=Parameter.empty, annotation=Parameter.empty)
- Gli oggetti Parameter sono immutable. Per modificare un oggetto Parameter si usa Parameter.replace() che crea una copia modificata dell’oggetto.
- attributi:
  - empty: un marcatore speciale per specificare l’assenza di valori di default e annotazioni.
  - name: il nome del parametro (stringa). Il nome deve essere un identificatore valido
  - default: il valore di default per il parametro. Se il parametro non ha valore di default questo attributo è settato a Parameter.empty
  - annotation: l’annotazione per il parametro. Se il parametro non ha annotazione, questo attributo è settato a Parameter.empty
  - kind: descrive come i valori degli argomenti vengono associati ai parametri
```python
from inspect import signature

def foo(a, b, *, c, d=10):
    pass

sig = signature(foo)
for param in sig.parameters.values():
    print('Parameter {}: {}'.format(param,param.kind))

>>> Parameter a: POSITIONAL_OR_KEYWORD
>>> Parameter b: POSITIONAL_OR_KEYWORD
>>> Parameter c: KEYWORD_ONLY
>>> Parameter d=10: KEYWORD_ONLY
```

Possibili valori di Parameter.kind: 

| **Dicitura**            | **Significato**                                                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `POSITIONAL_ONLY`       | Value must be supplied as a positional argument. Positional only parameters are those which appear before a `/` entry (if present) in a Python function definition. |
| `POSITIONAL_OR_KEYWORD` | Value may be supplied as either a keyword or positional argument (this is the standard binding behaviour for functions implemented in Python).                      |
| `VAR_POSITIONAL`        | A tuple of positional arguments that aren’t bound to any other parameter. This corresponds to a `*args` parameter in a Python function definition.                  |
| `KEYWORD_ONLY`          | Value must be supplied as a keyword argument. Keyword only parameters are those which appear after a `*` or `*args` entry in a Python function definition.          |
| `VAR_KEYWORD`           | A dict of keyword arguments that aren’t bound to any other parameter. This corresponds to a `**kwargs` parameter in a Python function definition.                   |

## metodi inspect.stack e inspect.trace
- inspect.stack()
  - restituisce una lista di oggetti FrameInfo per lo stack del caller. La prima entrata nella lista rappresenta il caller; l’ultima entrata rappresenta la chiamata più esterna nello stack.
- inspect.trace()
  - restituisce una lista di oggetti FrameInfo per lo stack tra il frame corrente e quello in cui un’eccezione che si sta gestendo è stata lanciata. La prima entrata nella lista rappresenta il caller; l’ultima entrata rappresenta dove è stata lanciata l’eccezione

## classe inspect.FrameInfo
è una sorta di tupla con i seguenti campi:
- frame: l’oggetto frame a cui corrisponde il record.
- filename: nome del file associato al codice che è eseguito dal frame che corrisponde a questo record
- lineno: il numero di linea della linea corrente associata al codice che è eseguito dal frame corrispondente a questo record
- function: Il nome della funzione che è stata eseguita dal frame a cui corrisponde questo record
- code_context: una lista di linee dal codice sorgente eseguito dal frame corrispondente a questo record
- index: L’indice della linea corrente che è eseguita nella lista del code_context.
- positions: un oggetto dis.Positions contenente il numero della linea iniziale, quello della linea finale, lo spazio davanti la colonna iniziale e quello davanti la linea finale associate all’istruzione eseguita dal frame corrispondente a questo record.
  - Il modulo dis supporta l’analisi del bytecode di CPython. class dis.Positions contiene i seguenti campi (alcuni sono None se l’informazione non è disponibile): lineno, end_lineno,col_offset , end_col_offset

## metodi inspect.getgeneratorstate e inspect.getgeneratorlocals
utili per determinare quando un generatore è in esecuzione o se è in attesa di cominciare l'esecuzione o riprenderla o se è terminato.
- inspect.getgeneratorstate(generator) restituisce lo stato di un generatore-iteratore.
  - possibili stati:
    - GEN_CREATED: In attesa di cominciare l’esecuzione.
    - GEN_RUNNING: In esecuzione.
    - GEN_SUSPENDED: Sospeso ad una espressione
    - GEN_CLOSED: Esecuzione completata.
- inspect.getgeneratorlocals(generator) restituisce il mapping tra le variabili “in vita” nel generatore e i loro valori correnti, cioe` un dizionario di coppie (nome,valore).
  - Cio` equivale ad invocare locals() dall’interno del generatore.
  - Se generator è un generatore senza un frame associato allora viene restituito un dizionario vuoto.
  - Viene lanciata TyperError se generator non è un oggetto generatore.


<table>
<tr>
<th> Codice </th>
<th> Output </th>
</tr>
<tr>
<td>

```python
import inspect
def gen():
    for i in range(10):
        X = yield i
        print("questo e` X nel generatore dopo che riprende l'esecuzione:", X)

generatore = gen()
print("Questo e` lo stato di generatore:",
      inspect.getgeneratorstate(generatore))
print("Queste sono le variabili locali in generatore:",
      inspect.getgeneratorlocals(generatore))
print("invoco next(generatore)")
print("next(generatore) produce: ", next(generatore))
print("Questo e` lo stato di generatore:",
      inspect.getgeneratorstate(generatore))
print("Queste sono le variabili locali in generatore:",
      inspect.getgeneratorlocals(generatore))
print("invoco send(77)")
print("send(77) restituisce il valore fornito dall’espressione yield nella seconda iterazione:",
      generatore.send(77))
print("Questo e` lo stato di generatore:",
      inspect.getgeneratorstate(generatore))
print("Queste sono le variabili locali in generatore:",
      inspect.getgeneratorlocals(generatore))
```

</td> <td>

```text
Questo e` lo stato di generatore: GEN_CREATED
Queste sono le variabili locali in generatore: {}
invoco next(generatore)
next(generatore) produce: 0
Questo e` lo stato di generatore: GEN_SUSPENDED
Queste sono le variabili locali in generatore: {'i': 0}
invoco send(77)
questo e` X nel generatore dopo che riprende l'esecuzione: 77
send(77) restituisce il valore fornito dall’espressione yield nella seconda iterazione: 1
Questo e` lo stato di generatore: GEN_SUSPENDED
Queste sono le variabili locali in generatore: {'i': 1, 'X': 77}
```
</td> </tr> </table>

## metodo inspect.getattr_static
- Funzionalità per accedere agli attributi in modo statico.
- Sia getattr() che hasattr() possono innescare l’esecuzione del codice quando ricercano il valore di un attributo o ne verificano l'esistenza.
- Nel caso in cui si desidere un’introspezione passiva, come quando si vuole accedere alla documentazione, questo comportamento potrebbe non essere conveniente e si può ricorrere ai seguenti metodi:
  - inspect.getattr_static(obj, attr, default=None) recupera gli attributi senza innescare la ricerca dinamica attraverso \_\_getattr__() o \_\_getattribute__()
- Si noti che questa funzione potrebbe non essere in grado di recuperare tutti gli attributi recuperabili da getattr() (come quelli creati dinamicamente) ma potrebbe trovare attributi non recuperabili da getattr() (come descrittori che lanciano AttributeError). Questa funzione può restituire descrittori invece che membri dell’istanza.

```python
import inspect
class foo_function:
    __slots__ = ['foo']

result = inspect.getattr_static(foo_function(), 'foo')
print(result)
result = getattr(foo_function(), 'foo')
print(result)

>>> <member 'foo' of 'foo_function' objects>
>>> Traceback (most recent call last):
>>> File "/Users/adb/Documents/didattica2/didattica/progAv2022/test_getattr_static.py", line 7, in
>>> <module>
>>> result = getattr(foo_function(), 'foo')
>>> AttributeError: 'foo_function' object has no attribute 'foo'
```
## metodo inspect.getmembers_static(object [,predicate])
- Restituisce tutti I membri di un oggetto in una lista di coppie (name,value) ordinate in base a name senza innescare la ricerca dinamica con \_\_getattr__ o \_\_getattribute__
- Se viene fornito predicate allora vengono restituiti solo i membri che soddisfano il predicato
- getmembers_static potrebbe non ruscire a fornire tutti i membri forniti da getmembers (come gli attribute create dinamicamente e può trovare membri che getmembers non può trovare (come descrittore che lanciano AttributeError). Inoltre in alcuni casi potrebbe resituire oggetti descriptor invece che istanze.

## classe inspect.Traceback
filename: Il nome del file associato al codice eseguito dal frame a cui corrisponde questo traceback.
lineno: il numero di linea della linea corrente associata al codice che è eseguito dal frame corrispondente a questo traceback
function: Il nome della funzione che è stata eseguita dal frame a cui corrisponde questo traceback.
code_context: una lista di linee dal codice sorgente eseguito dal frame corrispondente a questo traceback
index: L’indice della linea corrente che è eseguita nella lista del code_context.
positions: un oggetto dis.Positions contenente il numero della linea iniziale, quello della linea finale, lo spazio davanti la colonna iniziale e quello davanti la linea finale associate all'istruzione eseguita dal frame corrispondente a questo traceback.
<br><br>
inspect.getframeinfo(frame, context=1) Ottiene l’informazione riguardante un frame o di un oggetto traceback. Restituisce un oggetto traceback.
inspect.getouterframes(frame, context=1) Restituisce una lista di oggetti Frameinfo per frame e per tutti i frame più esterni le cui invocazioni hanno portato alla creazione di frame. Nella lista i frame sono ordinati a partire dal frame fino ad arrivare al frame più esterno nello stack di frame.
inspect.getinnerframes(traceback, context=1) Restituisce una lista di oggetti Frameinfo per il frame traceback e per tutti i frame più interni le cui invocazioni sono una conseguenza di frame.
<br><br>
Nella lista i frame sono ordinati a partire da traceback; l’ultima rappresenta il punto dove l’eccezione
è stata lanciata.
<br><br>
inspect.currentframe() restituisce l’oggetto frame per il frame che effettua l’invocazione. Questa funzione si basa sul supporto Python per i frame dello stack dell’interprete. Tale supporto esiste in CPython ma non è detto che esista in altre implementazioni, nel qual caso currentframe() restituisce None.
inspect.stack(context=1) restituisce una lista di oggetti Frameinfo per lo stack del frame che effettua l’invocazione. Nella lista i frame sono ordinati a partire dal frame che effettua l’invocazione fino ad arrivare al frame più esterno nello stack.


