# Comportamentale - Template Method

- È un Design Pattern comportamentale che permette di definire i passi di un algoritmo lasciando alle sottoclassi il compito di definire alcuni di questi passi.
- Vediamo un esempio con una classe AbstractWordCounder class che fornisce due metodi:
    - Il primo metodo can_count(filename) restituisce un booleano che indica se la classe può contare le parole del file dato in base all’estensione del file.
    - Il secondo metodo, count(filename) restituisce il conteggio di parole.
- Il codice comprende 2 sottoclassi, una che conta le parole in file di testo e l’altro per contare le parole in file HTML.
- Tutti i metodi sono statici e non si ha a che fare con le istanze della classe.

```python
def count_words(filename):
	for wordCounter in (PlainTextWordCounter, HtmlWordCounter):
		if wordCounter.can_count(filename):
			return wordCounter.count(filename)
```

```python
class AbstractWordCounter:

	@staticmethod
	def can_count(filename):
		raise NotImplementedError()

	@staticmethod
	def count(filename):
		raise NotImplementedError()
```

```python
class AbstractWordCounter(metaclass=abc.ABCMeta):

	@staticmethod
	@abc.abstractmethod
	def can_count(filename):
		pass

	@staticmethod
	@abc.abstractmethod
	def count(filename):
		pass
```

- Questa sottoclasse implementa il contatore per i file testuali e assume che i file con estensione .txt siano codificati con UTF-8

```python
class PlainTextWordCounter(AbstractWordCounter):
    @staticmethod
    def can_count(filename):
        return filename.lower().endswith(".txt")

    @staticmethod
    def count(filename):
        if not PlainTextWordCounter.can_count(filename):
            return 0

        regex = re.compile(r"\\w+")
        total = 0

        with open(filename, encoding="utf-8") as file:
            for line in file:
                for _ in regex.finditer(line):
                    total += 1
				return total

```