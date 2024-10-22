# Index of Python Exercises

## [1_python_standard](1_python_standard)

- [3_myDictionary.py](1_python_standard/1_myDictionary.py)

```text
Test per myDidictionary (si veda l'ultimo fascicolo di slide).
```
- [6_esercitazione.py](1_python_standard/2_esercitazione.py)

```text
Esercizio 5
Scrivere una classe di base ClsBase in cui c'è un metodo addAttr che controlla se la classe ha l'attributo di nome s
e se tale attributo non è presente, allora aggiungere l'attributo s con un valore v; in caso contrario non fa niente.
 Il metodo deve funzionare anche per le eventuali sottoclassi agendo sulla sottoclasse senza bisogno però di essere
 ridefinito nella sottoclasse.
```
- [9_classeC.py](1_python_standard/3_classeC.py)

```text
- Scrivere una classe C per cui accade che ogni volta che si aggiunge una variabile di istanza ad una delle istanze di C
 in realtà la variabile viene aggiunta alla classe come variabile di classe.
- Modificare la classe al punto precedente in modo tale che le istanze.

Modificare la classe al punto precedente in modo tale che le istanze abbiano al più due variabili di istanza:
varA e varB e non deve essere possibile aggiungere altre variabili di istanza oltre a queste due. Se il programma avesse
bisogno di aggiungere altre variabili oltre a quelle sopra indicate, queste altre variabili verrebbero create come
variabili di classe e non di istanza.
```

---
## [2_decorators](2_decorators)

- [10_fdecorator.py](2_decorators/6_fdecorator.py)

```text
Modificare la funzione al punto precedente in modo che la funzione decorata operi su qualsiasi elemento possa essere
convertito in int e che non si abbia errore se un elemento della lista non può essere convertito in int anche se è di un tipo
convertibile a int (ad esempio "anna")
```
- [11_decfact.py](2_decorators/7_decfact.py)

```text
Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo per contare il numero
di invocazioni del metodo passato come parametro al decorator factory
```
- [12_ClasseConFF.py](2_decorators/8_ClasseConFF.py)

```text
Scrivere un decorator factory che prende in input una classe ClasseConFF e due stringhe funz e ff e restituisce un
decoratore di classe che decora una classe in modo tale che se viene invocata funz di fatto al posto di funz viene
invocata la funzione ff della classe ClasseConFF
```
- [1_decorator.py](2_decorators/1_decorator.py)

```text
Dopo aver eseguito il programma una volta, il file risultato.txt deve contenere le seguenti linee:

io sono il risultato della funzione invocata con args=(1, 2) e kwargs={}
1
io sono il risultato della funzione invocata con args=(9,) e kwargs={'k': 2}
9
io sono il risultato della funzione invocata con args=() e kwargs={'j': 6, 'k': 3}
6
```
- [2_decorator.py](2_decorators/2_decorator.py)

```text
Scrivere il decoratore di funzione decora che trasforma la funzione decorata in una funzione che lancia l'eccezione TypeError
se uno o più argomenti non sono di tipo str. La funzione deve restituire una stringa formata dagli argomenti ricevuti in input e dal
risultato intervallati da uno spazio. Non dimenticate di convertire il risultato in stringa quando lo inserite nellaringa output.

Esempio: se la funzione riceve in input "il", "risultato", "è", la funzione non lancia l'eccezione e restituisce la stringa
"Il risultato è..." dove al posto dei puntini deve apparire il risultato della funzione
```
- [4_esercitazione.py](2_decorators/3_esercitazione.py)

```text
Dopo aver eseguito il programma una volta, il file risultato.txt deve contenere le seguenti linee:

io sono il risultato della funzione invocata con args=(1, 2) e kwargs={}
1
io sono il risultato della funzione invocata con args=(9,) e kwargs={'k': 2}
9
io sono il risultato della funzione invocata con args=() e kwargs={'j': 6, 'k': 3}
6
```
- [5_esercitazione.py](2_decorators/4_esercitazione.py)

```text
g prima di essere decorata e` una funzione che restituisce una stringa formata da 4 ripetizioni del primo argomento, se  c'e` almeno un argomento,
 altrimenti restituisce una stringa vuota. Fornisci la funzione decora
```
- [7_decorator_class.py](2_decorators/5_decorator_class.py)

```text
Scrivere un decoratore di classe che, se applicato ad una classe, la modifica in modo che funzioni
come se fosse stata derivata dalla seguente classe base. N.B. le classi derivate da ClasseBase non
hanno bisogno di modificare i metodi f() e g() e la variabile varC. Inoltre quando vengono create le
istanze di una classe derivata queste ’’nascono’’ con lo stesso valore di varI settato da __init__ di
ClasseBase.
```

---
## [3__new__and__init__](3__new__and__init__)

- [2_esercitazione.py](3__new__and__init__/2_esercitazione.py)

```text
Scrivere due classi Twin1 e Twin2 nessuna delle quali è derivata dell'altra. Le istanze di ciascuna classe devono
essere identiche e anche identiche alle istanze dell'altra classe (identiche vuol dire con stessi attributi). Non occorre
scrivere il codice per fare altro oltre a quanto richiesto
```
- [my_string.py](3__new__and__init__/my_string.py)

```text
Ridefiniscimi il comportamento della classe Stringa (str) in questo modo:
- attraverso una sua classe figlia in cui, utilizzando __new__ ridefinisca il comportamento della classe String ottenendo la stringa in Uppercase
```

---
## [4_generators](4_generators)

- [6_generatore.py](4_generators/6_generatore.py)

```text
Scrivere un generatore che ogni volta che è invocato stampa un elemento dalla lista e smette di stampare elementi
non appena incontra un elemento maggiore di 10
```
- [factorial_recursive_generator.py](4_generators/factorial_recursive_generator.py)
- [reverse_gen.py](4_generators/reverse_gen.py)

---
## [5_singleton](5_singleton)

- [placeholder.py](5_singleton/placeholder.py)

---
## [6_proxy](6_proxy)

- [1_esercitazione.py](6_proxy/1_esercitazione.py)

```text
Scrivere una classe MyProxy che è il proxy della classe MyClass. Ogni volta che viene invocato un metodo di istanza
della classe MyProxy, di fatto viene invocato l'omonimo metodo di istanza di MyClass. Non deve essere usata l'ereditarietà

- si assuma che __init__ di MyClass prenda in input un argomento x e che il comportamento dei suoi metodi di istanza
dipenda dal valore di x passati a __init__
```

---
