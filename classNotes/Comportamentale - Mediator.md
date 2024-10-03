# Comportamentale - Mediator

Fornisce un mezzo per creare un oggetto che incapsula le interazioni tra altri oggetti.

- Ciò consente di stabilire relazioni tra oggetti senza che questi abbiano conoscenza diretta l’uno dell’altro.
- Per esempio se si verifica un evento che richiede l’attenzione di alcuni oggetti, tale evento sarà comunicato al mediatore che manderà una notifica agli oggetti interessati.
- Il design pattern mediator evita il tight coupling (forte dipendenza tra un gruppo di oggetti)
    - rende possibile cambiare l’interazione tra gli oggetti senza dover apportare modifiche agli oggetti stessi.
    - facilita l’implementazione, il testing, la riusabilità degli oggetti.

### Esempio

- Vogliamo creare delle form contenenti text widget e button widget.
- Ciò è di grande utilità nella programmazione GUI
- L’intestazione tra i widget della form sarà gestita da un mediator.
- La classe Form fornisce i metodi `create_widgets()` e `create_mediator()`

```python
class Form:
	def __init__(self):
		self.create_widgets()
		self.create_mediator()

	def create_widgets(self): #questo crea il form
		self.nameText = Text()  #gli fornisce 2 campi di testo per il nome utente e l'email
		self.emailText = Text()
		self.okButton = Button("OK")  #un bottone OK
		self.cancelButton = Button("Cancel")  #un bottone cancella

	def create_mediator(self): #ogni form possiede un proprio mediator associato.
		self.mediator = Mediator(((self.nameText, self.update_ui), (self.emailText, self.update_ui), (self.okButton, self.clicked),(self.cancelButton, self.clicked)))
		#l'init di Mediator riceve come argomenti delle coppie (widget, callable) che descrive una relazione che il mediatore deve supportare
		self.update_ui()
#esempio: se cambia il testo nel widget invochiamo update_ui. Se viene cliccato uno dei bottoni allora si invoca Form.clicked() e così via

	def update_ui(self, widget=None):
		#abilita il bottone di conferma (ok) se entrambi i campi contengono del testo altrimenti rimane disabilitato
		self.okButton.enabled = (bool(self.nameText.text) and bool(self.emailText.test))

	def clicked(self, widget):
		#questo è uno dei metodi passati nel mediator. Stampa solo ok o cancella se il tasto premuto è il corrispondente
		if widget == self.okButton:
			print("OK")
		elif widget == self.cancelButton:
			print("Cancel")
```

- Il metodo Init della classe Mediator, come detto prima crea un dizionario di tipo defaultdict le cui chiavi sono widget e i cui valori sono liste di uno o più callable
- il for considera le coppie (widget, caller) presenti nella tupla passata come secondo argomento e le inserisce nel dizionario.
- Alla fine viene settato l’attributo mediator del widget in modo che contenga il mediato appena creato.

```python
class Mediator:
	def __init__(self, widgetCallablePairs):
		self.callablesForWidget = collection.defaultdict(list)
		for widget, caller in widgetCallablePairs:
			self.callablesForWidget[widget].append(caller)
			widget.mediator = self
	
	def on_change(self, widget):
	#ogni volta che un oggetto mediato cambia stato, esso invoca il metodo on_change che si occupa di invocare ogni metodo associato al widget
		callables = self.callablesForWidget.get(widget)
		if callables is not None:
			for caller in callables:
				caller(widget)
		else:
			raise AttributeError(f"No on_change() method registered for {widget}")
```

- Questa è una classe base per le classi mediate
- Le istanze della classe mantengono un riferimento all’oggetto mediatore.
- Il metodo Mediated.on_change() invoca il metodo on_change() del **Mediatore** passandogli il widget mediato su cui è stato invocato il metodo Mediated.on_change
- Siccome questa classe non è modificata da sottoclassi, essa rappresenta un esempio in cui è possibile rimpiazzare la classe base con un decoratore di classe.

```python
class Mediated:
	def __init__(self):
		self.mediated = None

	def on_change(self):
		if self.mediator is None:
			self.mediator.on_change(self)
```

- La classe Button estende Mediated e un oggetto bottone ha l’attributo self.mediator e il metodo on_change che viene invocato quando il botone cambia stato (quando è cliccato).

```python
class Button(Mediated):
	def __init__(self, text=""):
		super().__init__()
		self.enabled = True
		self.text = text
	
	def click(self):
		if self.enabled:
			self.on_change() #l'invocazione di click provoca l'invocazione di Button.on_change() che causa l'invocazione di on_change() del mediatore.
		#il metodo associato al botone in questo caso è Form.clicked() con il bottone stesso come argomento di tipo widget
```

- Un’altra classe mediata, per fare un esempio è Text

```python
class Text(Mediated):
		def __init__(self, text=""):
			super().__init__()
			self.__text = text

	@property
	def text(self):
		return self.__text

	@text.setter
	def text(self, text):
		if self.text != text:
			self.__text = text
			self.on_change()
```

```python
#Un programma che crea ed usa una form
def main():
	form = Form()
	test_user_interaction_with(form)
	
def test_user_interaction_with(form):
	form.okButton.click() # Ignorato perchè bottone disabiliato dalla chiamata a self.update_ui() in create_mediator()
	print(form.okButton.enabled) # False
	form.nameText.text = "Fred"
	print(form.okButton.enabled) # False perchè non basta aver inserito solo il nome
	form.emailText.text = "fred@bloggers.com"
	print(form.okButton.enabled) # True perchè; è stato inserito anche l’indirizzo mail
	form.okButton.click() # OK
	form.emailText.text = ""
	print(form.okButton.enabled) # False
	form.cancelButton.click() # Cancel

if __name__ == "__main__":
	main()
	
```

### Esempio basato su Coroutine

- Un mediatore si presta ad un’implementazione mediate coroutine perché può essere visto come una pipeline che riceve messaggi e passa questi messaggi agli oggetti interessati.
- In questo esempio viene implementato un mediator mediante coroutine per lo stesso problema considerato nell’esempio precedente.
- A differenza di quanto accadeva prima, in questa implementazione ogni widget è associato ad un mediatore che è una pipeline di coroutine (prima il mediatore era un oggetto associato all’intera form e tutti i widget della form erano associati insieme ai rispettivi callable al mediatore)
    - Ogni volta che un widget cambia stato, esso invia se stesso alla pipeline.
    - Sono le componenti della pipeline a decidere se svolgere o meno azioni in risposta al cambio di stato del widget.
- Nell’approccio precedente il metodo on_change() del mediatore invoca i metodi associati al widget nel caso in cui il widget cambia stato.
- Il codice non illustrato è identico a quello visto nell’esempio precedente.
- **Non abbiamo bisogno di creare una classe Mediated** perché è di fatto una pipeline di coroutine.
- Una volta creata la pipeline, l’attributo mediator della pipeline viene settato con questa pipeline.

```python
def create_mediator(self):
	self.mediator = self._update_ui_mediator(self._clicked_mediator())
	for widget in (self.nameText, self.emailText, self.okButton, self.cancelButton):
		widget.mediator = self.mediator
	self.mediator.send(None)
#viene inviato None alla fine della pipeline e siccome nessun Widget è None, nessuna azione
#specifica verrà intrapresa ad eccezione di azion che interessano la form
#come abilitare o disabilitare il bottone Ok
```

- Questa coroutine è parte della pipeline
- Ogni volta che un widget notifica un cambio di stato, il widget passato alla pipeline è restituito dall’espressione yield e salvato nella variabile widget.
- **Quando occorre abilitare o disabilitare il bottone Ok, questo viene fatto indipendentemente da quale widget abbia cambiato stato**
    - Potrebbe anche non cambiare stato di alcun widget e quindi inizializzare la Form.
    - Dopo aver settato enabled al bottone, la coroutine passa il widget alla chain

```python
@coroutine
def _update_ui_mediator(self, successor=None):
	while True:
		widget = (yield)
		self.okButton.enabled = (bool(self.nameText.text) and bool(self.emailText.text))
	
		if successor is not None:
			successor.send(widget)

@coroutine #si occupa solo dei pulsanti Ok e Cancel
def _clicked_mediator(self, successor=None):
	while True:
		widget = (yield)
		if widget == self.okButton:
			print("OK")
		elif widget == self.cancelButton:
			print("Cancel")
		elif successor is not None: #passa il widget alla prossima coroutine nella pipeline, se ve ne è una
			successor.send(widget)
```

L’unica cosa che cambia rispetto a prima è che la classe Mediated invia alla pipeline il widget nel metodo on_change()

```python
class Mediated:
	def __init__(self):
		self.mediator = None

	def on_change(self):
		if self.mediator is not None:
			self.mediator.send(self)
```

![Untitled](Untitled%203.png)