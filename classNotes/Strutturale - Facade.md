# Strutturale - Facade

Il design pattern facade fornisce un’interfaccia semplificata per un sistema costituito da interfacce o classi troppo complesse o troppo di basso livello.

- La libreria standardi di Python fornisce moduli per gestire file compressi gzip, tarballs e zip. Questi moduli hanno interfacce diverse.
- Immaginiamo di voler accedere ai nomi di un file di archivio ed estrarre i suoi file usando un’interfaccia semplice.
- **Soluzione**: usiamo Facade per fornire un’interfaccia semplice ed uniforme che delega la maggior parte del vero lavoro alla libreria standard.

![Untitled](Untitled%206.png)

```python
class Archive:
	
	def __init__(self, filename):
		self._names = None #contiene un callable che restituisce una lista dei nomi dell'archivio
		self._unpack = None #contiene un callable che estrae tutti i file dell'archivio nella directory corrente
		self._file = None #mantiene il file object che è stato aperto per accedere all'archivio
		self._filename = filename #è una proprietà che mantiene il nome del file di archivio

	@property
	def filename(self):
		return self._filename

	@filename.setter
	def filename(self, name):
		self.close() #chiude l'archivio
		self._filename = name #aggiorna la variabile filename

	def close(self): #quando hai finito
		if self._file is not None:
			self._file.close() #chiude il file object e aperto
		self._names = self._unpack = self._file = None #setta le variabili per invalidarle

	def __enter__(self):
		return self #restituisce l'istanza di archive

	def __exit__(self, exc_type, exc_value, traceback):
		self.close() #chiude se è aperto il file

	def _prepare(self):
		if self.filename.endswith((".tar.gz", ".tar.bz2", ".tar.xz", ".zip")):
			self._prepare_tarball_or_zip()
		elif self.filename.endswith(".gz")
			self._prepare_gzip()
		else:
			raise ValueError("unreadable: {}".format(self.filename))

	def names(self):
		if self._file is None:
			self._prepare() #pone i callable in _names e _unpack
		return self._names() #restituisce la lista dei nomi del file archivio

	def unpack(self):
		if self._file is None:
			self._prepare()
		self._unpack() #uguale a names ma non li restituisce

	def is_safe(self, filename):
		return not (filename.startswith(("/", "\\")) or (len(filename) > 1 and filename[1] == ":" and filename[0] in string.ascii_letter) or re.search(r"[.][.][/\\]", filename))
		#se spacchettato potrebbe sovrascrivere file di sistema rimpiazzandoli con file non funzionanti o pericolosi. Non dovrebbero mai essere aperti file contenenti path assoluti o che includo path relative
		#evitare di aprire archivi con privilegi di amministratore. Restituisce False anche se comincia con un forward slash o slash o comincia con D:, che è un'unità disco.
```

![codice mancante del funzionamento dell’estrazione di tarball e zip](Untitled%207.png)

codice mancante del funzionamento dell’estrazione di tarball e zip

![codice mancante del funzionamento dell’estrazione di gzip](Untitled%208.png)

codice mancante del funzionamento dell’estrazione di gzip

Il Pattern Facade permette di creare interfacce semplici e comode che ci permettono di ignorare dettagli di basso livello. Uno svantaggio di questo Design Pattern potrebbe essere quello di non consentire un controllo più fine. Tuttavia, facade non nasconde od elimina le funzionalità del sistema sottostante e così è possibile usare un facade passando a classi di più basso livello se necessitiamo di maggior controllo

```python
with Archive(zipFilename) as archive:
	print(archives.names())
	archive.unpack()
```

# Context Manager

I Context Manager ci consentono di allocare e rilasciare risorse quando vogliamo. Se ci sono errori durante l’utilizzo cerca di chiuderlo.

```python
with open('some_file' 'w') as opened_file:
	opened_file.write('Hola!')
```

```python
#codice equivalente
file = open('some_file', 'w')
try:
	file.write('Hola!')
finally:
	file.close()
```

È possibile implementare un Context Manager come una classe. È sufficiente definire __enter__() ed __exit__() per usare la classe in uno statement with

```python
class File:
	def __init__(self, file_name, method):
		self.file_obj = open(file_name, method)

	def __enter__(self):
		return self.file_obj

	def __exit__(self, type, value, traceback):
		self.file_obj.close()
```

**Come funziona lo Statement With**

- Immagazzina il metodo __exit__() della classe File
- Invoca il metodo __enter__() della classe File
    - il metodo __enter__ restituisce il file object per il file aperto
- L’object file è passato ad opened_file
- Dopo che è stato eseguito il blocco al suo interno, lo statement with invoca il metodo __exit__()
    - chiude il file
- Se tra il momento in cui viene passato l’object file a opened_file e il momento in cui viene invocata la exit si verifica un’eccezione, Python passa type, value e traceback dell'eccezione agli argomenti di __exit__() per gestire l’eccezione. In questo caso decide come chiudere il file e se eseguire altri passi. In questo esempio gli argomenti che vengono passati sono ignorati ed il comportamento default è chiudere il file.
    - Se __exit__() restituisse True, l’eccezione NON verrebbe rilanciata dallo statement with.
    - Se __exit__() restituisse un altro valore l’eccezione verrebbe lanciata dallo statement with
    - Nel nostro esempio restituisce None per cui lancia l’eccezione.
    
    ```python
    class File(object):
    	def __init__(self, file_name, method):
    		self.file_obj = open(file_name, method)
    
    	def __enter__(self):
    		return self.file_obj
    
    	def __exit__(self, type, value, traceback):
    		print("Exception has been handled")
    		self.file_obj.close()
    		return True
    
    with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()
    ```
    
    ### Context Manager e Generatori
    
    È possibile implementare un context manager con un generatore utilizzando il modulo contextlib. Il decoratore Python contextmanager trasforma il generatore in un oggetto GeneratorContextManager
    
    ```python
    from contextlib import contextmanager
    @contextmanager
    def open_file(name):
    	f = open(name, 'w’)
    	yield f
    	f.close()
    ```
    
    ```python
    with open_file('some_file’) as f:
    f.write('hola!')
    ```
    
    ```python
    from contextlib import contextmanager
    @contextmanager
    def open_file(name):
    	f = open(name, 'w’)
    	try:
    		yield f
    	finally:
    		f.close()
    ```