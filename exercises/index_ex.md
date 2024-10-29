# Index of Python Exercises

## [1_python_standard](1_python_standard)

- [1_myDictionary.py](1_python_standard/1_myDictionary.py)

```text
Test per myDidictionary (si veda l'ultimo fascicolo di slide).
```
- [2_esercitazione.py](1_python_standard/2_esercitazione.py)

```text
Esercizio 5
Scrivere una classe di base ClsBase in cui c'è un metodo addAttr che controlla se la classe ha l'attributo di nome s
e se tale attributo non è presente, allora aggiungere l'attributo s con un valore v; in caso contrario non fa niente.
 Il metodo deve funzionare anche per le eventuali sottoclassi agendo sulla sottoclasse senza bisogno però di essere
 ridefinito nella sottoclasse.
```
- [3_classeC.py](1_python_standard/3_classeC.py)

```text
- Scrivere una classe C per cui accade che ogni volta che si aggiunge una variabile di istanza ad una delle istanze di C
 in realtà la variabile viene aggiunta alla classe come variabile di classe.

Modificare la classe al punto precedente in modo tale che le istanze abbiano al più due variabili di istanza:
varA e varB e non deve essere possibile aggiungere altre variabili di istanza oltre a queste due. Se il programma avesse
bisogno di aggiungere altre variabili oltre a quelle sopra indicate, queste altre variabili verrebbero create come
variabili di classe e non di istanza.
```
- [4__mro__.py](1_python_standard/4__mro__.py)

```text
- Scrivere la classe ClasseB che ha il metodo di istanza contaVarClasse(self, t, n) che:
    - prende in input un tipo t e un intero n
    - restituisce il numero di variabili di classe di tipo t delle prime n classi della gerarchia formata dalla classe
      in cui self è istanza e dalle sue superclassi, le prime n secondo l'ordine indicato in __mro__. Se il numero di 
      classi nella suddetta gerarchia è minore di n allora vengono considerate tutte le classi della gerarchia.
    
    -NB: gli attributi di classe o istanza di classe o modulo sono mantenuti in un dizionario detto __dict__ che è a sua
     volta un attributo dell'oggetto.
    - vars({object}) restituisce il __dict__ per il modulo, classe o istanza dotata di __dict__.
```
- [5_static&class_methods.py](1_python_standard/5_static&class_methods.py)

```text
- Scrivere una classe Impiegato e due sottoclassi Tecnico e Amministrativo.
- In aggiunta al metodo __init__, la classe Impiegato può avere solo un altro metodo, mentre le due sottoclassi possono
  avere solo __initi__
- Scrivere poi un programma che crei un certo numero di istanze delle tre classi e stampa il numero di: tecnici,
  amministratori e il totale di impiegati (può essere maggiore della somma di tecnici e amministratori, in quanto è
  possibile avere impiegati 'generici')
```
- [intercorso1_1.py](1_python_standard/intercorso1_1.py)

```text
- Scrivere una classe di base ClsBase in cui c’è un metodo addAttr che:
    - Prende in input due argomenti: una stringa s e un valore v
    - Controlla se la classe ha l’attributo di nome s e se tale attributo non è presente allora aggiunge alla classe
      l’attributo s con valore v; in caso contrario non fa niente
    - Il metodo deve funzionare anche per le eventuali sottoclassi di ClsBase
```

---
## [2_decorators](2_decorators)

- [1_decf.py](2_decorators/1_decf.py)

```text
- Scrivere il decoratore di funzione decf che fa in modo che venga lanciata l'eccezione 'TypeError' se il numero di
  argomenti è diverso da due. Altrimenti, se la funzione decorata restituisce un risultato, questo viene aggiunto
  insieme al valore del primo argomento in un file di nome 'risultato.txt'.
- Suggerimento: ricorda di convertire a stringa il valore del primo argomento e il risultato quando li scrivete nel file
  e di aprire il file in modo da NON cancellare quanto scritto precedentemente nel file.
```
- [2_decorator.py](2_decorators/2_decorator.py)

```text
Scrivere il decoratore di funzione decora che trasforma la funzione decorata in una funzione che lancia l'eccezione TypeError
se uno o più argomenti non sono di tipo str. La funzione deve restituire una stringa formata dagli argomenti ricevuti in input e dal
risultato intervallati da uno spazio. Non dimenticate di convertire il risultato in stringa quando lo inserite nellaringa output.

Esempio: se la funzione riceve in input "il", "risultato", "è", la funzione non lancia l'eccezione e restituisce la stringa
"Il risultato è..." dove al posto dei puntini deve apparire il risultato della funzione
```
- [3_esercitazione.py](2_decorators/3_esercitazione.py)

```text
NOTA: non è ben nota la traccia dell'esercizio, è stata ricostruita ad occhio vedendo il comportamento atteso.
- Scrivi una funzione decf che lanci l'eccezione TypeError se il numero di argomenti passati alla funzione decorata è
  superiore a 2. Altrimenti, procedi con l'esecuzione della funzione.
```
- [4_esercitazione.py](2_decorators/4_esercitazione.py)

```text
g prima di essere decorata e` una funzione che restituisce una stringa formata da 4 ripetizioni del primo argomento, se  c'e` almeno un argomento,
 altrimenti restituisce una stringa vuota. Fornisci la funzione decora
```
- [5_decorator_class.py](2_decorators/5_decorator_class.py)

```text
Scrivere un decoratore di classe che, se applicato ad una classe, la modifica in modo che funzioni
come se fosse stata derivata dalla seguente classe base. N.B. le classi derivate da ClasseBase non
hanno bisogno di modificare i metodi f() e g() e la variabile varC. Inoltre quando vengono create le
istanze di una classe derivata queste ’’nascono’’ con lo stesso valore di varI settato da __init__ di
ClasseBase.
```
- [6_fdecorator.py](2_decorators/6_fdecorator.py)

```text
Modificare la funzione al punto precedente (?) in modo che la funzione decorata operi su qualsiasi elemento possa essere
convertito in int e che non si abbia errore se un elemento della lista non può essere convertito in int anche se è di un tipo
convertibile a int (ad esempio "anna")
```
- [7_decfact.py](2_decorators/7_decfact.py)

```text
Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo per contare il numero
di invocazioni del metodo passato come parametro al decorator factory
```
- [8_ClasseConFF.py](2_decorators/8_ClasseConFF.py)

```text
Scrivere un decorator factory che prende in input una classe ClasseConFF e due stringhe funz e ff e restituisce un
decoratore di classe che decora una classe in modo tale che se viene invocata funz di fatto al posto di funz viene
invocata la funzione ff della classe ClasseConFF
```
- [esame_1.py](2_decorators/esame_1.py)

```text
- scrivere nel file un decorator factory decFact che prende in input un tipo t e restituisce un decoratore di classe
  decorator che dota la classe decorata di un metodo di istanza 'addToList' che restituisce una lista contenente i nomi
  e i valori delle variabili di tipo t dell'istanza per cui è invocato. Ciascuna coppia (nome, valore) deve essere all'
  interno di una tupla. Il codice della classe non deve essere modificato.
```
- [esame_2.py](2_decorators/esame_2.py)

```text
Scrivere nel file un decorator factory DecoratorFactF che prende in input un valore v e restituisce un decoratore di
funzione che modifica il comportamento della funzione decorata come segue:
- se la funzione è invocata con tutti gli argomenti di tipo uguale a quello di v allora la funzione restituisce lo
  stesso valore che avrebbe restituito la funzione originaria;
- se uno o più argomenti sono di tipo diverso da quello di v allora la funzione restituisce il valore che la funzione
  originaria avrebbe restituito se fosse stata invocata solo su tutti gli argomenti dello stesso tipo di v;
- se la funzione originaria lancia un'eccezione, questa deve essere lanciata anche dalla funzione decorata.
```
- [intercorso1_1.py](2_decorators/intercorso1_1.py)

```text
- Scrivere nel file un decorator factory decFact(L1, L2) che prende in input una lista L1 di stringhe e una lista L2 di
  oggetti e produce un decoratore di classe che fa in modo che le istanze della classe nascano non solo con le variabili
  di istanza aggiunte al metodo __init__ della classe ma anche con le seguenti variabili di istanza:
  - per ogni i = 0, ... , len(L1) -1, una variabile con un nome uguale a L1[i] e valore uguale a L2[i]. Nel caso in cui
    il metodo __init__ della classe originaria aggiunge già una variabile di istanza con lo stesso nome di una di quelle
    aggiunte dal decoratore, allora il valore della variabile deve essere quello assegnato da __init__ della classe
    originaria.
```
- [intercorso1_2.py](2_decorators/intercorso1_2.py)

```text
- Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo statico che
  restituisce il numero di invocazioni del metodo passato come parametro al decorator factory
```
- [intercorso1_3.py](2_decorators/intercorso1_3.py)

```text
- Scrivere un decorator factory decFact che restituisce un decoratore che dota la classe decorata di un metodo statico
  riportaVariabiliDiClasse che non prende in input alcun argomento.
  Il metodo restituisce un generatore di triple. Ciascuna tripla contiene come primo elemento il nome di una variabile
  di classe, come secondo elemento il valore della suddetta variabile e come terzo elemento la classe in cui viene
  trovata la variabile (potrebbe essere C o una delle sue superclassi)
```

---
## [3__new__and__init__](3__new__and__init__)

- [1_esercitazione.py](3__new__and__init__/1_esercitazione.py)

```text
Scrivere due classi Twin1 e Twin2 nessuna delle quali è derivata dell'altra. Le istanze di ciascuna classe devono
essere identiche e anche identiche alle istanze dell'altra classe (identiche vuol dire con stessi attributi). Non occorre
scrivere il codice per fare altro oltre a quanto richiesto
```
- [2_my_string.py](3__new__and__init__/2_my_string.py)

```text
Ridefiniscimi il comportamento della classe Stringa (str) in questo modo:
- attraverso una sua classe figlia in cui, utilizzando __new__ ridefinisca il comportamento della classe String ottenendo la stringa in Uppercase
```
- [esame_1.py](3__new__and__init__/esame_1.py)

```text
Scrivere nel file la classe MySet che estende frozenset in modo tale che quando si crea l'istanza di MySet, l'istanza
creata contenga solo gli elementi di tipo int dell'oggetto iterabile passato come argomento a MySet(). Se MySet() non
prende input niente, l'istanza creata è vuota.
```
- [intercorso1_StrangeClass.py](3__new__and__init__/intercorso1_StrangeClass.py)

```text
Fornire la classe StrangeClass che funziona in modo tale che la seconda istanza creata sia identica alla prima,
la quarta sia identica alla terza e così via. Istanze vengono considerate identiche se nascono identiche e lo restano
durante la loro intera vita
```

---
## [4_generators](4_generators)

- [1_generatore.py](4_generators/1_generatore.py)

```text
Scrivere un generatore che ogni volta che è invocato stampa un elemento dalla lista e smette di stampare elementi
non appena incontra un elemento maggiore di 10
```
- [2_factorial_recursive_generator.py](4_generators/2_factorial_recursive_generator.py)

```text
- Scrivere una funzione generatrice myGenerator(n) che prende in input un intero n>=1 e restituisce un
iteratore dei primi n faForiali. In altre parole, la prima volta che viene invocato next viene restituito 1!,
la seconda volta 2!, la terza volta 3!, e così via fino ad n!.
- Bonus: se la funzione generatrice è definita ricorsivamente è consentito scrivere una funzione generatrice
  ricorsiva che prende in input più parametri e che viene opportunamente invocata da myGenerator
```
- [3_reverse_gen.py](4_generators/3_reverse_gen.py)

```text
Scrivere un generatore che data una lista la restituisce al contrario (?)
```
- [intercorso1_1.py](4_generators/intercorso1_1.py)

```text
- Scrivere nel file una funzione generatrice generaQuadratoInput che prende come argomento un intero m>=1 e restituisce
  un iteratore dei quadrati degli interi via via digitati dall'utente fino a quando gli interi digitati sono minori o
  uguali di m. Più precisamente, se it è l'iteratore generato da generaQuadratoInput(m) allora ogni volta che viene digi
  tato next(it).
- Il programma si mette in attesa che l'utente digiti qualcosa (seguito da return) e se l'utente digita un intero minore
  o uguale di m allora next(it) restituisce il quadrato dell'intero digitato. Se invece:
        - l'intero digitato è maggiore di m,
        - o l'utente digita qualcosa che non è un intero
        - o interrompe l'esecuzione del programma,
 l'iteratore it smette di funzionare
```
- [intercorso1_2.py](4_generators/intercorso1_2.py)

```text
- Scrivere una funzione che prende in input un intero positivo n e un valore sentinella
  e restituisce un generatore degli interi
- L’i-esimo elemento è (0+1+2+…+i-1). Se ad un certo punto raggiunge o supera il valore di sentinella
  allora l’iteratore smette di funzionare
```
- [intercorso1_3.py](4_generators/intercorso1_3.py)

```text
- Scrivere nel file esercizio1.py una funzione generatrice generaElementi che prende in input una lista L di elementi
  a due a due distinti e permette di ottenere un iteratore che scandisce gli elementi della lista nel seguente modo:
    - la prima volta che viene invocato next si ottiene il primo elemento della lista L[0]
    - per le invocazioni successive di next si ha il seguente comportamento:
        - sia L[i] l'elemento generato con l’invocazione di next
        - Se L[j] è un intero k diverso da j e compreso tra 1 e len(L)-1 allora la prossima invocazione di next
          restituisce L[k]
        - In caso contrario non vengono generati altri elementi e le invocazioni successive di next causano un'eccezione
    - Se L=[2, 8, 4, 'a', 3] allora le prime con le prime 4 invocazioni di next otteniamo 2 4 3 'a'
      mentre la quinta invocazione causa una StopIteration
```
- [intercorso1_decFact(L1L2).py](4_generators/intercorso1_decFact(L1L2).py)

```text
Scrivere nel file esercizio3.py un decorator factory decFact(L1,L2) che prende in input una lista di stringhe e una
stringa di oggetti e produce un decoratore di classe che fa in modo che le istanze della classe nascano non solo con le
variabili di istanza aggiunte dal metodo __init__ della classe ma anche con le seguenti variabili di istanza:
    - per ogni i = 1... len(1) una variabile con nome uguale a quello della i-esima stringa di L1 e valore uguale
      all'i-esimo oggetto di L2. Nel caso in cui __init__ della classe originaria aggiungeva già una variabile di
      istanza con nome uguale all'i-esima stringa di L1 allora il valore della variabile deve essere quello assegnato da
      __init__ della classe originaria.
```
- [intercorso1_generaElementi.py](4_generators/intercorso1_generaElementi.py)

```text
Scrivere nel file esercizio1.py una funzione generatrice generaElementi che prende in input una lista L di elementi a
due a 2 distinti (Non c'è bisogno di controllare che siano distinti). Scandisce la lista nel seguente modo:
- la prima volta che viene invocato next si ottiene il primo elemento della lista L[0]
- per le invocazioni successive di next si ha il seguente comportamento:
    - sia L[j] l'elemento generato con la più recente invocazione di next. Se L[j] è un intero k diverso da j e compreso
      tra 1 e len(L)-1 allora la prossima invocazione di next restituisce L[k]. In caso contrario non vengano generati
      altri elementi e le invocazioni successive di next causano un'eccezione.

  ES: L=[2, 8, 4, 'a', 3] allora le prime con le prime 4 invocazioni di next otteniamo 2 4 3 'a' mentre la quinta
  invovcazione causa StopIteration
```

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
## [7_chain_of_responsability](7_chain_of_responsability)

- [1_esercizio.py](7_chain_of_responsability/1_esercizio.py)

```text
- Scrivere una funzione che prende in input una sequenza di richieste (liste di 2 interi) e passa ciascuna richiesta ad
  una catena di gestori ciascuno dei quali è una coroutine.
- Se il primo intero della lista è nell'intervallo [0, 4] allora la richiesta viene gestita da Handler_04 che stampa
  "Richiesta {} gestita da Handler_04.
- Se il primo intero nella lista è nell'intervallo [5, 9] allora la richiesta viene gestita da Handler_59 che
  "Richiesta {} gestita da Handler_59.
- Se il primo intero della lista è maggiore di 9 allora la richiesta viene gestita da Handler_gt9 che stampa:
  "Messaggio da Handler_gt9: non è stato possibile gestire la richiesta {}. Richiesta modificata".
    - Dopo aver effettuato la stampa, Handler_gt9 sottrae al primo intero della lista il secondo intero della lista e lo
      invia nuovamente ad una nuova catena di gestori.
- Se la richiesta non è una lista di 2 numeri o il primo intero della lista è minore di 0 la richiesta viene gestita da
  Default_Handler che stampa semplicemente
  "Richiesta {} gestita da Default_Handler: non è stato possibile gestire la richiesta"
- Nelle suddette stampe, la lista nella richiesta deve comparire al posto delle parentesi graffe
```

---
