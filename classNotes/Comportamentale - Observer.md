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

HistoryView è un osservatore e fornisce un metodo update() che accetta il modello osservato come suo unico argomento. Ogniqualvolta il metodo update() è invocato, esso aggiunge una tupla alla sua lista data in questo modo la storia di tutti i cambiamenti applicati al modello rimarrà salvata al suo interno.

```python
class HistoryView:

	def __init__(self):
		self.data = []

	def update(self, model):
		self.data.append((model.value, time.time())
```

LiveView è un altro osservatore e rappresenta il numero di celle usate per rappresentare il valore del modello in una riga della tabella HTML. Il metodo update è invocato quando il modello è osservato per la prima volta e quando viene successivamente aggiornato. 

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
	historyView = = HistoryView()
	liveView = LiveView()
	model = SliderModel(0, 0, 40) 
	model.observer_add(historyView, liveView)
	for value in (7, 23, 37):
		model.value = value
	for value, timestamp in historyView.data:
		print("{:3} {}".format(value, datetime.datetime.fromtimestamp(timestamp)), file=sys.stderr)
```

![Untitled](Untitled%204.png)

![Untitled](Untitled%205.png)