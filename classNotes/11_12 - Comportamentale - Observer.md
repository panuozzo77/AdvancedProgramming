# Comportamentale - Observer

Il pattern observer supporta relazioni di dipendenza tra oggetti in modo tale che quando un oggetto cambia stato tutti gli oggetti collegati sono informati del cambio.

- Tipicamente si tratta di gestire una relazione di dipendenza one-to-many tra un oggetto osservato e degli osservatori e l’obiettivo è di fare in modo che gli oggetti non siano strettamente accoppiati.
- Il design pattern observer evita che l’oggetto osservato aggiorni direttamente gli oggetti ad esso collegati in quanto ciò determinerebbe un accoppiamento stretto tra l’oggetto osservato e gli osservatori

Uno degli esempi di questo pattern e delle sue varianti è l’MVC che consiste nel separare un’applicazione in tre componenti logiche: model, view e controller.

In termini di Observer, le view sono osservatori del modello ed il modello è l’oggetto di osservazione.

### Esempio

- Consideriamo un modello che rappresenta un valore con un minimo e un massimo, come ad esempio una scrollbar o un controllo della temperatura.
- Vengono creati 2 osservatori (view) separati per il modello:
    - uno per dare in output il valore del modello ogni volta che esso cambia sotto forma di una barra di progressione in formato HTML;
    - l’altro per mantenere la storia del cambiamento; (timestamp)
    
#### Classe Observed
- observers_add() accetta uno o più osservatori da aggiungere. Per questo motivo oltre a *observer c'è il parametro observer che assicura che il numero di osservatori passati in input al metodo non sia zero.
- usa nel for il metodo intertools.chain(*iterables) che crea un iteratore che restituisce gli elementi dell'oggetto iterabile specificato come primo argomento e quando non ci sono più elementi da restituire in questa lista, passa alla prossima collezione iterabile e così via fino a che non vengono restituiti gli elementi di tutte le collezioni iterabili in iterables. Il for non avrebbe potuto usare la concatenazione di tuple in questo modo "for observer in (observer,) + observers:"

```python
class Observed:
	def __init__(self):
		self.__observers = set()

	def observers_add(self, observer, *observers):
		for observer in itertools.chain((observer,), observers):
			self.__observers.add(observer)
			observer.update(self) #viene invocato per inizializzare l'osservatore con lo stato attuale del modello
	
	def observer_discard(self, observer):
		self.__observer.discard(observer)

	def observers_notify(self): #se il modello cambia stato, invoca questo metodo
		for observer in self.__observers:
			observer.update(self)  #si assicura che tutti gli altri osservatori effettuino un altro check
```

#### Classe SliderModel
- La classe SliderModel eredita dalla classe Observed un insieme privato di osservatori che inizialmente è vuoto e i metodi observers_add(), observer_discard() e observers_notify().
- Quando lo stato del modello cambia, per esempio quando il suo valore cambia, esso deve invocare il metodo observers_notify() in modo che ciascun osservatore possa rispondere di conseguenza.
- SliderModel ha anche le proprietè minimum e maximum i cui setter, come quello di value, invocano il metodo observers_notify().

```python
class SliderModel(Observed):
	def __init__(self, minimum, max, value):
		super().__init__()
		self.__minimum = self.__value = self.__maximum = None
		self.minimum = minimum
		self.value = value
		self.maximum = maximum

	@property
	def value(self)
		return self.__value

	@value.setter
	def value(self, value):
		if self.__value != value:
			self.__value = value
			self.observers_notify()
```

#### Classe HistoryView
- HistoryView è un osservatore e fornisce un metodo update() che accetta il modello osservato come suo unico argomento. 
- Ogniqualvolta il metodo update() è invocato, esso aggiunge una tupla alla sua lista data in questo modo la storia di tutti i cambiamenti applicati al modello rimarrà salvata al suo interno.

```python
class HistoryView:

	def __init__(self):
		self.data = []

	def update(self, model):
		self.data.append((model.value, time.time())
```

#### Classe LiveView
- LiveView è un altro osservatore e rappresenta il numero di celle usate per rappresentare il valore del modello in una riga della tabella HTML. 
- Il metodo update è invocato quando il modello è osservato per la prima volta e quando viene successivamente aggiornato. 
  - Stampa una tabella HTML di una riga con un numero self.length di celle per rappresentare il modello. Le celle sono di colore ciano se sono vuote e blu scuro altrimenti.

```python
class LiveView:
	def __init__(self, length=40):
		self.length = length

	def update(self, model):
		tippingPoint = round(model.value * self.length / (model.maximum - model.minimum))
		td = '<td style="background-color: {}">&nbsp;</td>'
		html = ['<table style="font-family: monospace" border="0"><tr>']
		html.extend(td.format("darkblue") * tippingPoint)
		html.extend(td.format("cyan") * (self.length - tippingPoint))
		html.append("<td>{}</td></tr></tables>".format(model.value))
		print("".join(html)

```

```python
def main():
	historyView = HistoryView()
	liveView = LiveView()
	model = SliderModel(0, 0, 40) 
	model.observer_add(historyView, liveView)
	for value in (7, 23, 37):
		model.value = value
	for value, timestamp in historyView.data:
		print("{:3} {}".format(value, datetime.datetime.fromtimestamp(timestamp)), file=sys.stderr)
```

# Esercizio su Observer
Scrivere una classe LaureaT_Student che possa essere osservata e che possieda i seguenti attributi che ne determinano lo stato:
- total_cfu: numero di CFU acquisiti.
- english_r: valore booleano impostato su False (valore predefinito) se e solo se lo studente non ha superato la prova di inglese.
- grades: dizionario degli esami sostenuti, in cui le chiavi corrispondono ai nomi degli esami e i valori ai voti ottenuti (nome dell'esame, voto).
- exam: una tupla del tipo definito di seguito:
  - Exam = collections.namedtuple("Exam", "name cfu").

- Gli attributi total_cfu ed english_r sono accessibili direttamente tramite il loro nome e possono essere modificati con l'operatore =. L'attributo grades, invece, è modificabile attraverso il metodo add_grades, che accetta come primo argomento un oggetto di tipo Exam e come secondo argomento un intero che rappresenta il voto. Inoltre, è necessario implementare due observer: HistoryView e LiveView. 
- HistoryView mantiene una lista di triple della forma (dizionario degli esami sostenuti, booleano che indica se l'esame di inglese è stato superato, data del cambiamento di stato). Ogni tripla viene creata quando l'oggetto LaureaT_Student cambia stato.
- LiveView esegue le seguenti stampe:
  - print("Cambio stato: lo studente ha appena superato la prova di Inglese\n") se il cambiamento di stato è dovuto al superamento della prova di inglese.
  - print("Cambio stato: lo studente ha superato un nuovo esame").
  - print("Cambio stato: il numero di CFU è: ", student.total_cfu, "\n") se il cambiamento di stato è dovuto al superamento di un nuovo esame.
